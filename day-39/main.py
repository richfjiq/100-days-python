from data_manager import DataManager
from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
cities_data = DataManager()
data = cities_data.getCitiesData()
pprint(data)
