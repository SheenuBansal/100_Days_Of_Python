# with open("weather_data.csv") as fileobject :
#     texts = fileobject.readlines()
#     print(texts)

# ------------------------------------------------------------------
# import csv 

# with open("weather_data.csv") as data_file :
#     data = csv.reader(data_file)
#     temperatures=[]
#     for row in data :
#         # print(row)
#         temperatures.append(row[1])

#     new_temperatures = []
#     for i in range(1,len(temperatures)-1) :
#         new_temperatures.append(int(temperatures[i]))

#     print(new_temperatures)

# ------------------------------------------------------------------------------------

import pandas
# data = pandas.read_csv("weather_data.csv")

# Print Tables data
# print(data)

# Print any single column
# print(data["temp"])
# print(data.temp)

# Find Mean of Temp column 
# print(pandas.Series.mean(data["temp"]))
# print(data["temp"].mean())

# Find Max Temp
# print(data["temp"].max())

# NOTE : data["temp"] is same as data.temp . The first method calls like dictionary method we studied and later one calls
# like the objects.

# Fetch a particular value from table, say Monday
# print(data[data["day"] == "Monday"])

# Fetch a row, where temp was max
# print(data[data["temp"] == data["temp"].max()])

# Fetch a particular value in the row which we have found out by applying some criteria
# monday = data[data["day"] == "Monday"]
# print(monday.condition)

# Convert Monday's temperature to Fahrenheit
# monday = data[data["day"] == "Monday"]
# monday_temp = int(monday.temp)*9/5 + 32
# print(monday_temp)

# create a dataframe from scratch
# students={
#     "students" : ["Shalini","Rohini","Mabelline"],
#     "scores" : [23,17,19]
# }

# data = pandas.DataFrame(students)
# data.to_csv("students.csv")

