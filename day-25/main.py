# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # average = sum(temp_list) / len(temp_list)
# # print(average)

# # Average temperature
# print(data["temp"].mean())

# # max temp
# print(data["temp"].max())

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in row
# print(data[data.day == "Monday"])

# Get row with highest temperature in th week
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# # throw a warning
# # monday_temp = int(monday.temp)

# # Removes the warning
# monday_temp = int(monday.iloc[0, 1])
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
# Create file
data.to_csv("new_data.csv")
