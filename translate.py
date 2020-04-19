# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:35:03 2020

@author: Wiktoria
"""

from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate('How are you?', dest= 'es')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data=data)
    json_data = json.loads(response.text)
    print(type(json_data))
    print(json_data['contents']['translated'])
    
piratetrans('hello sir')
