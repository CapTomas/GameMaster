from generate import generate_prompt
from generate import call_openai
from random import randint
import db_static
from time import sleep
import logging
import concurrent.futures
from eleven_labs import generate_audio

skill = "novice"
# Difficulty will be set by the players in the future, and will range between novice, casual, standard, advanced, hardcore.
difficulty = "advanced"
players = {}
discussion = ""

data = None
websockets = {}
user_states = {}
processing = False

def inject_data(_data):
    global data
    data = _data

def set_websocket(user_id, websocket):
    global websockets
    websockets[user_id] = websocket

# Welcome new player.
async def welcome(user_id, character_id):
    # Global is bad here
    global websockets, user_states, players
    state = {}
    user_states[user_id] = state

    websocket = websockets[user_id]
    character = data.get_character(character_id, True)
    prompt = generate_prompt("introduction/introduce_realm")
    introduction = call_openai(prompt, 256)
    executor = concurrent.futures.ThreadPoolExecutor()
    executor.submit(generate_audio, introduction.replace('\n', '\n\n'))
    # Shutdown the executor without waiting for tasks to complete.
    executor.shutdown(wait=False)
    sleep(3)
    await websocket.send("NARRATION: " + introduction.replace('\n', '\n\n'))

    # You can retrieve the result later with future.result() if needed
    # prompt = generate_prompt("interactions/introduce_player_character", (character[0], character[2] ))
    # introduction = call_openai(prompt, 512)
    # await websocket.send("NARRATION:" + introduction.replace('\n', '\n\n'))

    await load(user_id)

async def sendAll(message, excluded = None):
    print("Sending...")
    for playersocket in websockets.values():
        if playersocket != excluded:
            await playersocket.send(message)

async def load(user_id):
    global websockets, user_states, players
    state = {}
    user_states[user_id] = state
    websocket = websockets[user_id]
    # Load settings from previous state.
    character = data.get_user_character(user_id, True)
    print ("here ok")
    players[character[0]] = user_id
    realm_id = character[5]
    realm = data.get_realm(realm_id)
    state['character'] = list(character)
    state['realm'] = list(realm)
    state['realm_id'] = realm_id
    state['websocket'] = websocket

    await sendAll("SYSTEM:LOGIN!" + character[0], websocket)
#    await handle_interactions(user_id)

# async def handle_interactions(user_id):
 # TODO here should be some logic to handle interactions 
    # await handleMessage(state, message)


# async def handleMessage(state, message):
    # TODO here should be some logic to handle messages from players
