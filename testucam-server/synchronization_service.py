from threading import Thread
from collections import Counter
import datetime

import speech_service
import os

from aiortc.contrib.media import MediaPlayer
from peerconnection import pc

looking_at_queue = []
most_common = None
last_update = datetime.datetime.now()

names = {

}

def add_to_queue(new_value):
    global most_common 
    global last_update 

    if len(looking_at_queue) == 5:
        looking_at_queue.pop(0)
    looking_at_queue.append(new_value)
    
    previous_most_common = most_common
    most_common = Counter(looking_at_queue).most_common(1)[0][0]

    if most_common != previous_most_common and most_common in names:
        speech_service.text_to_wav(f"en-US-Wavenet-B", f"{names[most_common]} is looking at you!")
        player = MediaPlayer(os.path.join(os.path.dirname(__file__), "demo-instruct.wav"))
        pc.addTrack(player.audio)

    last_update = datetime.datetime.now()

    print(looking_at_queue)
    print(names)

def get_looking_at():
    print(f"Most common: {most_common}")
    last_update_diff = datetime.datetime.now() - last_update
    if last_update_diff.seconds > 2:
        return None
    
    return most_common

def set_name(name):
    looking_at = get_looking_at()
    print(f"Attempting to set name of {looking_at} to {name}")
    if looking_at is not None:
        names[looking_at] = name