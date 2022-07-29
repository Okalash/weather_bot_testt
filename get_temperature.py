import json
import requests
from datetime import datetime
from time import sleep
import logger

logger_temp = logger.Logger()

def get_temp(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "0b387297c7msh8834bc6ab8ef67ep17d705jsn0515e91d5c71",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    # get request
    r = requests.get(url, headers=headers, params=querystring)
    data = dict(eval(r.text))
    # write to file to test
    logger_temp.write_to_json(data)

    temp_far = data['current_observation']['condition']['temperature']
    temp_cel = int((temp_far - 32) * (5 / 9))

    return temp_cel

# print(datetime.now().strftime("%H:%M:%S"), str(get_temp(city)) + "°C")
# while True:
#     sleep(10)
#     print(datetime.now().strftime("%H:%M:%S"), str(get_temp(city)) + "°C")
