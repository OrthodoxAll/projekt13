import os
import pytest
from sys import path
from unittest.mock import patch
import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY1= os.getenv('API_KEY')

def get_cord(city_name: str)->tuple:
    """Получение координат по названию города"""
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY1}')
    lat = response.json() [0]['lat']
    lon = response.json() [0]['lon']
    print(lat, lon)
    return lat, lon


def get_weather(lat:float,lon: float)->tuple:
    """Функция которая показывает погоду по координтам"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY1}')

    return (response.json()['main']['temp'])



@patch('requests.get')
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {'main': {'temp': 1}}
    assert get_weather(1,1) == 1
    mock_get.assert_called_once_with(f'https://api.openweathermap.org/data/2.5/weather?lat=1&lon=1&appid={API_KEY1}')


# lat, lon = get_cord('Moscow')
#
# print(get_weather(lat, lon))