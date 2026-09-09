import requests

API_KEY= 'c8bcab3d51bdef0326e31492773dc13e'
city_name = 'Moscow'
response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}')

print(response.json())