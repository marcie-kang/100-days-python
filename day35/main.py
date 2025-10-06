import requests
from twilio.rest import Client

account_sid = "AC613d945af87b79fa978840aed75f1781"
auth_token = "a4e51eb019206a2d6c481ffe7c62d597"

parameters = {
    "id": 2174003,
    "appid": "c86fe3cd5c9d9bbb8f99a069ef3322f5"
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
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+61490923543"
    )

    print(message.status)
