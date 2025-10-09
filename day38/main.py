import requests
from datetime import datetime

WEIGHT_KG = 55
HEIGHT_CM = 163
AGE = 29

APP_ID = "d7ae2ce5"
API_KEY = "103ca355f6986b8a70d95c4da568d1e3"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ac8fca49b778837d3ecd00b697edde5f/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint, json=user_params, headers=nutrition_headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_params, auth=("soromee", "yess"))

    print(sheet_response)
