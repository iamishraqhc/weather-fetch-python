import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

city = input('Enter the name of the city: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    weather = data['weather'][0]['description']
    temperature = data["main"]["temp"] - 273
    print('Weather: ', weather)
    print('Temperature: ', temperature, '\N{DEGREE SIGN}C')

else:
    print('There might be an error')
