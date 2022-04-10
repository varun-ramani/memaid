from threading import Thread
from collections import Counter

looking_at_queue = [-1]

def add_to_queue(new_value):
    if len(looking_at_queue) == 5:
        looking_at_queue.pop(0)
    looking_at_queue.append(new_value)

def get_mode():
    return Counter(looking_at_queue).most_common(1)[0][0]