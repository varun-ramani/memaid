import requests
from google.cloud import speech
url = 'https://language.googleapis.com//v1/documents:analyzeEntities'
myobj = {'key': 'Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones.'}

x = requests.post(url, data = myobj)
print(x.text)
