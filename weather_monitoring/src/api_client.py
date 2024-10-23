import requests
import configparser

class WeatherAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        self.api_key = config['API']['api_key']
        self.base_url = config['API']['base_url']

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json() if response.status_code == 200 else None
