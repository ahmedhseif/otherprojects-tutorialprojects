import smtplib
import datetime as dt
import random

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("quotes.txt") as file:
        contents = file.readlines()
        message = random.choice(contents)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ahmedseifpython@outlook.com",
            msg=f"Subject:Monday Motivation\n\n{message}"
        )




