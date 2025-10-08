import requests
from datetime import datetime

USERNAME = "soromee"
TOKEN = "jdflajflaj"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20250616"

today=datetime.now()

pixel_config = {
    "quantity": "1.0",
}

requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20250616"

requests.delete(url=pixel_endpoint, headers=headers)
