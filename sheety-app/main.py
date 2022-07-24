import os
import requests
from datetime import datetime

APP_ID = "2f5f88af"
API_KEY = "a8417627df0205cf9f198dc9ffd1447d"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/409426e3d7d4010d79a4396a8fe5c528/workoutTracking/workouts"



headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

request_body = {
    "query": input("what did you do: "),
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 163,
    "age": 23
}

response = requests.post(url=EXERCISE_ENDPOINT, json=request_body, headers=headers)
exercises = response.json()["exercises"]


# NO USE IG? /// headers_sheety = {
#     "Content-Type": "application/json"
# }


auth_headers = {
    "Authorization": "Basic YWhtZWRzZWlmOTg6ZmFibm9zdWZicXcxMg=="
}


for n in range(len(exercises)):
    name = exercises[n]["name"].title()
    duration = exercises[n]["duration_min"]
    calories = exercises[n]["nf_calories"]

    time_now = datetime.now()
    date = time_now.strftime("%d/%m/%Y")
    time = time_now.strftime("%H:%M:%S")

    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=auth_headers)




