import requests
from twilio.rest import Client

account_sid = "."
auth_token = "."

parameters = {
    "id": 0,
    "appid": "."
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
data_in_12_hours = data["list"][:12]
weather_hours = data["list"][0]["weather"][0]["id"]

will_rain = False

for hour in data_in_12_hours:
    condition_code = int(hour["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+0",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+0"
    )

    print(message.status)
