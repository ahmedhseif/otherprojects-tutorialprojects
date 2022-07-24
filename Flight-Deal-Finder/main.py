# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

datamanager = DataManager()
flightsearch = FlightSearch()
notification_manager = NotificationManager()
sheet_data = datamanager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flightsearch.get_destination_code(city["city"])
    datamanager.destination_data = sheet_data
    datamanager.update_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flightsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Only £{flight.price} to fly from {flight.origin_airport}-{flight.origin_city} to {flight.destination_airport}-{flight.destination_city}, from {flight.out_date} to {flight.return_date}"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}"

        users = datamanager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        # notification_manager.send_sms(message)
        notification_manager.send_email(emails, message, link)

