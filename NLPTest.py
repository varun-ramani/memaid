from http.client import responses
import requests as re
import os
from google.cloud import language_v1
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-file.json'
def sample_analyze_entities(text_content):
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
        print(u"Representative name for the entity: {}".format(entity.name))
        entity_type = language_v1.Entity.Type(entity.type_).name
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))
        if entity_type == "PERSON":
            persons.append(entity.name)
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))

            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            )
        print(" -------- NEXT THING ---------- ")
    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))
    
    return response, persons

text_content = "Hey, it's beautiful weather we're having today, isn't it? Yeah I love going to bitcamp and hacking. Oh yeah what's up by the way. And I use arch. Barbara has been getting on my nerves lately though. I'm hungry. She's a real pain."

response, persons = sample_analyze_entities(text_content)
looking_for = "my name is"
name_start = text_content.lower().find(looking_for)
if name_start != -1:
    print(" *********** THIS HERE *****************")
    name_rest = text_content[name_start + len(looking_for) + 1:]
    name = name_rest[:name_rest.find(" ")]
    name = name.strip()
    punctuation = "!\"'(),.:;?`"
    for character in punctuation:
        name = name.replace(character, '')
    
    print(name)
elif text_content.lower().find("i'm") != -1:
    name_start = text_content.lower().find("i'm")
    name_rest = text_content[name_start + len("i'm") + 1:]
    name = name_rest[:name_rest.find(" ")]
    punctuation = "!\"'(),.:;?`"
    for character in punctuation:
        name = name.replace(character, '')
    
    if name in persons:
        print(name)

