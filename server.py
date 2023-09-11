# BROKEN IT NEEDS FRONT END TO WORK, WILL DO LATER

import asyncio
import bcrypt
import logging
import pathlib
import ssl
import websockets

from random import randint

import characters
import players

# Constants to represent various message codes.
GM = "GM"
UNKNOWN = "UNKNOWN"
CHALLENGE = "CHALLENGE:"
SUCCESS = "SUCCESS"
EXISTING_USER = "EXISTINGUSER"

class WebSocketServer:
    def __init__(self):
        # A data member to hold references to some external data. 
        # Injected using the `inject_data` method.
        self.data = None

    def inject_data(self, data):
        """Inject external data into the server."""
        self.data = data

    async def _send_and_receive(self, websocket, message):
        """Send a message to the client and wait for a response."""
        await websocket.send(message)
        return await websocket.recv()

    async def _challenge_user(self, websocket, user):
        """
        Challenge the user by sending them a salt. If the response matches
        the expected hashed password, confirm authentication.
        """
        await websocket.send(f"{CHALLENGE}{user[3]}")
        response = await websocket.recv()
        if response and response == user[2]:
            await websocket.send(SUCCESS)
            players.set_websocket(user[0], websocket)
            await players.load(user[0])
            return user
        return None

    async def _handle_authentication(self, websocket, response):
        """Handle user authentication based on the provided username."""
        username = response[5:]
        user = self.data.get_user_by_username(username)
        if user:
            return await self._challenge_user(websocket, user)
        logging.warning(f"Unidentified user: {username}")
        await websocket.send(UNKNOWN)
        return None

    async def _register_new_user(self, websocket, username, salt):
        """Register a new user and generate an initial character for them."""
        password = await websocket.recv()
        user_id = self.data.add_user(username, password, salt)
        character_id = characters.generate_character('novice', user_id)
        players.set_websocket(user_id, websocket)
        await websocket.send(SUCCESS)
        await players.welcome(user_id, character_id)
        return user_id

    async def _handle_registration(self, websocket, response):
        """Handle user registration. If the username already exists, inform the client."""
        username = response[9:]
        user = self.data.get_user(username)
        if user:
            await websocket.send(EXISTING_USER)
            return None
        salt = bcrypt.gensalt().decode()
        await websocket.send(f"{CHALLENGE}{salt}")
        return await self._register_new_user(websocket, username, salt)

    async def handle_player(self, websocket, _):
        """Handle incoming player connections and determine if they're authenticating or registering."""
        try:
            logging.info("New connection established.")
            response = await self._send_and_receive(websocket, GM)
            if response:
                if response.startswith("AUTH:"):
                    await self._handle_authentication(websocket, response)
                elif response.startswith("REGISTER:"):
                    await self._handle_registration(websocket, response)
        except Exception as e:
            logging.error(f"Error handling connection: {str(e)}")
            # Consider adding cleanup or disconnecting the websocket.

    async def listen(self, url="localhost", port=9289, secure=False):
        """Start the WebSocket server. Can be set to secure (SSL/TLS) mode."""
        start_msg = "secure" if secure else "unsecured"
        logging.info(f"Listening for {start_msg} connections on {url}:{port}")
        ssl_context = None
        if secure:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_context.load_cert_chain(pathlib.Path(__file__).with_name('localhost.pem'))
        async with websockets.serve(self.handle_player, url, port, ssl=ssl_context):
            await asyncio.Future()  # run forever
