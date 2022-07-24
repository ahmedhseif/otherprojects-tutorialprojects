import datetime as dt
import pandas
import random
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_day = today.day
today_month = today.month
PLACEHOLDER = "[NAME]"
MY_EMAIL = "YOUR EMAIL"
MY_PASS = "YOUR PASSWORD"
birthday = pandas.read_csv("birthdays.csv")

for (index, row) in birthday.iterrows():
    if row.month == today_month and row.day == today_day:
        name = row["name"]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_chosen = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_chosen}.txt") as letter:
            contents = letter.read()
            new = contents.replace(PLACEHOLDER, name)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject:Happy Birthday {name}!\n\n{new}")


# 4. Send the letter generated in step 3 to that person's email address.




