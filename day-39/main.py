from data_manager import DataManager
from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
cities_data = DataManager()
sheet_data = cities_data.get_sheet_data()
pprint(sheet_data)
cities_data.update_iata_code()
