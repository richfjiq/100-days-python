import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels],
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
