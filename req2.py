import requests
import random
import time
import json
from cities import cities
from data import data
from words import words


url = 'https://prolifewhistleblower.com/anonymous-form/'

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

i=0
while (i < 10):
    # populate payload
    payload = {}
    for key in data.keys():
        info = 'Placeholder'
        if key == 'txtarea':
            info = ' '.join(random.sample(words, 40))
        if key == 'txt1':
            info = ' '.join(random.sample(words, 4))
        if key == 'txt6':
            info = 'Dr. ' + random.choice(list(cities.items()))[0]
        if key == 'txt2':
            info = random.choice(list(cities.items()))[0]
        if key == 'txt3':
            info = 'Texas'
        if key == 'txt4':
            info = random.randint(10000, 99999)
        if key == 'txt5':
            info = random.choice(list(cities.items()))[1]
        payload[key] = info

    response = requests.post(url, data=json.dumps(payload), headers=header)

    if response.status_code == 200:
        print('Success!')
    else:
        print('Fail.')
    
    i+=1
    time.sleep(5)

