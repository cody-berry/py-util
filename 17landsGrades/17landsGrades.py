# Testing section

# Section 1: Testing mean on a distribution.
import numpy as np
# distribution = []
# done = False
#
# # Input a distribution
# while not done:
#     dataPoint = input("Enter a number: ")
#     try:
#         dataPoint = float(dataPoint)
#         distribution.append(dataPoint)
#         done = True
#     except:
#         print("Invalid number")
#
# done = False
#
# while not done:
#     dataPoint = input("Enter a number (or enter a non-number to say \"done\"): ")
#     try:
#         dataPoint = float(dataPoint)
#         distribution.append(dataPoint)
#         print(distribution)
#     except:
#         done = True
#
#
# print(distribution)
#
# mean = 0
# for dataPoint in distribution:
#     mean += dataPoint
# mean /= len(distribution)
#
# print("mean: ", mean)
# print("mean from numpy: ", np.mean(distribution))
#
# stDev = 0
# for dataPoint in distribution:
#     stDev += (mean - dataPoint)**2
# stDev /= len(distribution)
# stDev **= 0.5
#
# print("standard deviation: ", stDev)
# print("standard deviation from numpy: ", np.std(distribution))

# Opens the csv and puts it in a list dictionaries
import csv
import json

data = []

# utf-8 encoding without the byte order mark
# parse the csv data into a list of dictionaries for each card
with open("./cardRatings/card-ratings-2023-06-22.csv", "r", encoding="utf-8-sig") as csvData:
    csvReaderResult = csv.DictReader(csvData)
    for row in csvReaderResult:
        data.append(row)

# dump the list of dictionaries into a json file
with open("./jsonCardRatings/card-ratings.json", "w") as jsonFile:
    # write the json.dumps output with an indent of 4 to the json file
    jsonFile.write(json.dumps(data, indent=4))

# print the name and game in hand win rate of each card
with open("./jsonCardRatings/card-ratings.json", "r") as jsonFile:
    jsonData = json.load(jsonFile)

    # calculate the mean
    mean = 0
    data = []
    for card in jsonData:
        if (card["GIH WR"]):
            mean += float(card["GIH WR"][:-1])
            data.append(float(card["GIH WR"][:-1]))
    mean /= len(jsonData)
    print("mean:", str(mean) + "%")
    print("numpy mean:", np.mean(data))

    # calculate the standard deviation
    stdev = 0
    for card in jsonData:
        if (card["GIH WR"]):
            stdev += (float(card["GIH WR"][:-1]) - mean)**2
    stdev /= len(jsonData)
    stdev **= 0.5
    print("standard deviation:", stdev)
    print("standard deviation numpy:", np.std(data))

    # print the card data
    for card in jsonData:
        if (card["GIH WR"]):
            print(str((float(card["GIH WR"][:-1]) - mean)/stdev)[:5], "  ", card["GIH WR"], "  ", card["Name"])
        else:
            print("Not enough data for:", card["Name"])



