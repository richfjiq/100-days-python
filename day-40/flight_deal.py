from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
users_data = data_manager.users_data
flight_search = FlightSearch()
notification_manager = NotificationManager()


ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    data_manager.update_iata_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight_data = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )

    if flight_data is None:
        continue

    if flight_data.price < destination["lowestPrice"]:
        for user in users_data:
            notification_manager.send_emails(
                price=flight_data.price,
                departure_city_name=flight_data.origin_city,
                departure_iata_code=flight_data.origin_airport,
                arrival_city_name=flight_data.destination_city,
                arrival_iata_code=flight_data.destination_airport,
                outbound_date=flight_data.out_date,
                inbound_date=flight_data.return_date,
                user_email=user["email"],
            )
