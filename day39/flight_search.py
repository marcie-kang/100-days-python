import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = "Bc2RLtgpahMipK5vJdfqQSpVlGrPKA67"
        self.AMADEUS_API_SECRET = "fTKziIMnGlxF4h8H"
        self.access_token = self.get_access_token()

    def get_access_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.AMADEUS_API_KEY,
            "client_secret": self.AMADEUS_API_SECRET
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception("토큰 발급 실패:", response.text)

    def search_city(self, keyword):
        url = "https://test.api.amadeus.com/v1/reference-data/locations"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        params = {
            "keyword": keyword,
            "subType": "CITY"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            results = response.json()['data']
            for city in results:
                print(f"{city['name']} ({city['iataCode']}) - {city['address']['countryName']}")
        else:
            raise Exception("도시 검색 실패:", response.text)
