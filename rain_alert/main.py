import requests

from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "ACe6007b4eda72b44cf44f8026f1917be4"
auth_token = "b0e7d9769aa840ed677c76fb4dc58cc3"

weather_params = {
    "lat": 39.165325,
    "lon": -86.526382,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella.",
        from_='+17376373457',
        to='+201096365437'
    )
    print(message.status)
# for n in range(12):
#     print(weather_data[n]["weather"][0]["id"])


