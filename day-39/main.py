from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    data_manager.update_iata_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
