from dotenv import load_dotenv, dotenv_values
import os
import requests

load_dotenv()
city_name = "lagos"
# print(os.getenv('API_key'))
# API_key= 'f9bda9f30ab08d4703164c774491d336'
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('API_key')}&units=metric"

response = requests.get(url)
if response.status_code == 200:
   
    data = response.json()
    print(f'the weather in {city_name} is', data['weather'][0]['description'])
    print(f'the current temprature in {city_name} is', data['main']['temp'])
    print('current humudity is', data['main']['humidity'])


