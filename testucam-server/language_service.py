from queue import Queue
from threading import Thread
from http.client import responses
from time import sleep
from cv2 import bilateralFilter
import requests as re
import os
from google.cloud import language_v1

import synchronization_service

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-file.json'

transcription_queue = Queue()

def sample_analyze_entities(text_content):
    bullet_points = []
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    persons = []
    # Loop through entitites returned from the API
    for entity in response.entities:
        entity_type = language_v1.Entity.Type(entity.type_).name
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        if entity_type == "PERSON":
            persons.append(entity.name)
        # Get the salience score associated with the entity in the [0, 1.0] range
        if entity.salience > 0.05:
            bullet_points.append(entity.name)

    print(bullet_points)
    
    return persons, bullet_points

def add_transcription(sentence):
    transcription_queue.put(sentence)

my_name = "Mark"
def start_language_service():
    global my_name
    while True:
        if not transcription_queue.empty():
            next_transcription = transcription_queue.get()
            # check if we're looking at something
            persons, bullet_points = sample_analyze_entities(next_transcription)
            looking_for = "my name is"
            punctuation = "!\"'(),.:;?`"
            name_start = next_transcription.lower().find(looking_for)
            if name_start != -1:
                name_rest = next_transcription[name_start + len(looking_for) + 1:]
                name = name_rest[:name_rest.find(" ") + 1]
                name = name.strip()
                for character in punctuation:
                    name = name.replace(character, '')
                if name.lower() != my_name.lower():
                    synchronization_service.set_name(name)
            elif next_transcription.lower().find("i'm") != -1:
                name_start = next_transcription.lower().find("i'm")
                name_rest = next_transcription[name_start + len("i'm") + 1:]
                name = name_rest[:name_rest.find(" ") + 1]
                for character in punctuation:
                    name = name.replace(character, '')
                
                if name in persons and name.lower() != my_name.lower():
                    synchronization_service.set_name(name)

            synchronization_service.set_topics(bullet_points)

        sleep(0.05)

language_service_thread = Thread(target=start_language_service)
language_service_thread.start()
