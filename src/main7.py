import os
import requests
from dotenv import load_dotenv
load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

def get_cord(city_name: str)->tuple:
    """Получение координат по названию города"""
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}')
    # lat = response.json() [0]['lat']
    # lon = response.json() [0]['lon']
    # print(lat, lon)
    # return lat, lon
    print(response.json())

def get_weather(lat:float,lon: float)->tuple:
    """Функция которая показывает погоду по координтам"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
    print(response.json())

get_cord('Moscow')

# print(get_weather(lat, lon))


