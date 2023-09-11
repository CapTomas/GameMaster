import asyncio
import db_dynamic
import db_static
import server
import characters
import players
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

async def main():
    """
    Main asynchronous function that initializes and starts the WebSocket server.
    
    - Initializes a new WebSocket server instance.
    - Injects shared data into various game modules.
    - Initializes the game database.
    - Starts listening for incoming WebSocket connections.
    """
    
    # Create an instance of the WebSocketServer from the server module.
    websocket_server = server.WebSocketServer()
    
    # Inject shared data into various game components.
    # This can be thought of as passing a shared resource or context
    # to multiple parts of the game's architecture.
    websocket_server.inject_data(db_dynamic)
    characters.inject_data(db_dynamic)
    players.inject_data(db_dynamic)
    
    # Initialize the game's database.
    db_dynamic.initialize_database()
    db_static.initialize_database()

    # Log a message indicating that the server is starting.
    logging.info("----- Starting server -----\n")

    # Begin listening for incoming WebSocket connections.
    await websocket_server.listen()

# Use asyncio to run the main asynchronous function.
# This effectively starts the game server and begins listening for client connections.
asyncio.run(main())
