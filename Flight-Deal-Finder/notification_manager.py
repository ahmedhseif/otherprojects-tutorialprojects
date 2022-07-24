from twilio.rest import Client
import smtplib
import requests

account_sid = "ACe6007b4eda72b44cf44f8026f1917be4"
auth_token = "b0e7d9769aa840ed677c76fb4dc58cc3"
MY_EMAIL = "ahmedseifpython@gmail.com"
MY_PASS = "pythonFTW123"


class NotificationManager:

    # This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, message):
        client = Client(account_sid, auth_token)
        sms = client.messages \
            .create(
            body=message,
            from_='+17376373457',
            to='+201096365437'
        )
        print(sms.sid)

    def send_email(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n"
                                        f"{message}\n{google_flight_link}".encode('utf-8')
                                    )
