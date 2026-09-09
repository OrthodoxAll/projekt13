import requests

API_KEY= 'c8bcab3d51bdef0326e31492773dc13e'

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&appid={API_KEY}')