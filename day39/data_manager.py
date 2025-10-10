import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ac8fca49b778837d3ecd00b697edde5f/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": "Bearer helo"
        }
        self.cities = []
        self.search_city()

    def search_city(self):
        url = "https://api.sheety.co/ac8fca49b778837d3ecd00b697edde5f/flightDeals/prices/1"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            results = response.json()
            print(results)
        else:
            raise Exception("토큰 발급 실패:", response.text)

