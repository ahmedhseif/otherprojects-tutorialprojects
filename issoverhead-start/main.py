import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.044420  # Your latitude
MY_LONG = 31.235712  # Your longitude
MY_EMAIL = "EMAIL"
MY_PASS = "PASS"


def iss_close_to_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False


def currently_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunrise < time_now < sunset:
        return False
    else:
        return True


while True:
    time.sleep(60)
    if iss_close_to_me() and currently_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="ahmedseifpython@outlook.com",
                                msg="Subject:Look up\n\nISS COMING ABOVE YOU!"
                                )

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
