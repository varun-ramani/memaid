from re import L
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
        speech_service.text_to_wav(f"en-US-Wavenet-B", f"{names[most_common]['name']} is looking at you!")
        os.system("vlc --vout none --no-video --play-and-exit output.wav")

        if 'topics' in names[most_common]:
            speech_service.text_to_wav(f"en-US-Wavenet-B", f"Last time, you talked about {'and'.join(names[most_common]['topics'])}")
            os.system("vlc --vout none --no-video --play-and-exit output.wav")

    last_update = datetime.datetime.now()

    print(names)

def get_looking_at():
    last_update_diff = datetime.datetime.now() - last_update
    if last_update_diff.seconds > 2:
        return None
    
    return most_common

def set_name(name):
    looking_at = get_looking_at()
    if looking_at is not None:
        if looking_at not in names:
            names[looking_at] = {}

        names[looking_at]['name'] = name

def set_topics(topics):
    looking_at = get_looking_at()
    if looking_at is not None:
        if looking_at in names:
            names[looking_at]['topics'] = topics