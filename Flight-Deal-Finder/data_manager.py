import requests
from pprint import pprint
SHEETY_ENDPOINT= "https://api.sheety.co/409426e3d7d4010d79a4396a8fe5c528/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/409426e3d7d4010d79a4396a8fe5c528/flightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        self.destination_data = requests.get(url=SHEETY_ENDPOINT).json()["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=body)
            print(response.text)


    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data