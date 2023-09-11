from generate import generate_prompt, call_openai
import logging
import db_static

data = None

def inject_data(_data):
    global data
    data = _data


def generate_character(level, user_id = None):
    logging.info("----- Generating Character -----")
    realm = db_static.get_realm()
    cnt = 0

## TODO need to add some character generation code here based on db_static. RACES & CLASSES