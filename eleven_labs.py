from elevenlabslib import *

user = ElevenLabsUser("ee9172f9eeb6ba2077bf42db43727fd8")
voice = user.get_voices_by_name("Ethan")[0]  # This is a list because multiple voices can have the same name

def generate_audio(text):
    return voice.generate_play_audio_v2(text, playbackOptions=PlaybackOptions(runInBackground=True))

    for historyItem in user.get_history_items_paginated():
        if historyItem.text == text:
            historyItem.delete()
            break