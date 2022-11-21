import requests
import json
from datetime import date
import pandas as pd
import numpy as np

api_key = "67b3c90d61ed464cc4dba385252c47be"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    
    response = requests.get(api_url)
    response_dict = response.json()
    #print(response_dict)
    weather = response_dict["weather"][0]["description"]

    if response.status_code == 200:
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
    return None