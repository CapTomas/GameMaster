from generate import generate_prompt
from generate import call_openai
from random import randint
import db_static
import logging

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
async def welcome(user_id, character_id, realm_id = 1):
    # Global is bad here
    global websockets, user_states, scenario, players
    state = {}
    user_states[user_id] = state

    websocket = websockets[user_id]
    character = data.get_character(character_id, True)
    realm = db_static.get_realm()
    prompt = generate_prompt("introduction/introduce_realm")
    introduction = call_openai(prompt, 256)
    await websocket.send("NARRATION: " + introduction.replace('\n', '\n\n'))
    exit()
    prompt = generate_prompt("interactions/introduce_player_character", (character[0], character[2] ))
    introduction = call_openai(prompt, 512)
    await websocket.send("NARRATION:" + introduction.replace('\n', '\n\n'))

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
