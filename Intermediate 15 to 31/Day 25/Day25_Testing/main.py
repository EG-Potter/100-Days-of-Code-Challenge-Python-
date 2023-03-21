# with open("weather_data.csv") as data_csv:
#     data = data_csv.readlines()
#     print(data)

# import csv.
#
# with open("weather_data.csv") as data_csv:
#     data = csv.reader(data_csv)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Panda import.
# import pandas
#
# # converts the CSV into data.
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(type(data["temp"]))
# #
# # # Creates Dictionary from Data.
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # # Calculates average from List.
# # temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# # # Simplified.
# # print(data["temp"].mean())
# # #  Max of Numbers.
# # print(data["temp"].max())
# #
# # Get Data in Row.
# print(data[data.day == "Monday"])
# # Get Data in Row.
# print(data[data.temp == data["temp"].max()])
#
#
# monday = data[data.day == "Monday"]
# convert = (monday["temp"]*9/5)+32
# print(convert)
#
#
# # Create a dataframe from scratch.
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

#
# data_dict = {
#     "Fur Color": ["Cinnamon", "Gray", "Black"],
#     "Count": []
# }
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# colours = ["Cinnamon", "Gray", "Black"]
# for color in colours:
#     temp = data["Primary Fur Color"] == color
#     data_dict["Count"].append(temp.sum())
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")
# print(data)
