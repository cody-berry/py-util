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

cardNames = []

# print the name and game in hand win rate of each card
with open("./jsonCardRatings/card-ratings.json", "r") as jsonFile:
    jsonData = json.load(jsonFile)
    jsonDataDict = {}

    # calculate the mean
    mean = 0

    # new dataset needed to account for cards without enough data
    data = []
    for card in jsonData:
        if (card["GIH WR"]):
            mean += float(card["GIH WR"][:-1])
            data.append(float(card["GIH WR"][:-1]))
    mean /= len(data)
    print("mean:", str(mean) + "%")

    # calculate the standard deviation
    stdev = 0
    for card in jsonData:
        if (card["GIH WR"]):
            stdev += (float(card["GIH WR"][:-1]) - mean)**2
    stdev /= len(data)
    stdev **= 0.5
    print("standard deviation:", stdev)

    print("Overall data:")
    print("   zscore   gihwr   name")

    # print the card data
    for i in range(0, len(jsonData)):
        card = jsonData.pop()
        cardNames.append(card["Name"])
        if (card["GIH WR"]):
            zScore = (float(card["GIH WR"][:-1]) - mean)/stdev

            # calculate the grade based on the z-score
            grade = "  "  # use this as extra spacing

            # S range
            if (zScore > 3):
                grade = "S+"
            elif (zScore > 2.75):
                grade = "S "
            elif (zScore > 2.5):
                grade = "S-"
            # A range
            elif (zScore > (2.5 - 1/3)):
                grade = "A+"
            elif (zScore > (1.5 + 1/3)):
                grade = "A "
            elif (zScore > 1.5):
                grade = "A-"
            # B range
            elif (zScore > (1.5 - 1/3)):
                grade = "B+"
            elif (zScore > (0.5 + 1/3)):
                grade = "B "
            elif (zScore > 0.5):
                grade = "B-"
            # C range
            elif (zScore > (0.5 - 1/3)):
                grade = "C+"
            elif (zScore > (-0.5 + 1/3)):
                grade = "C "
            elif (zScore > -0.5):
                grade = "C-"
            # D range
            elif (zScore > (-0.5 - 1/3)):
                grade = "D+"
            elif (zScore > (-1.5 + 1/3)):
                grade = "D "
            elif (zScore > -1.5):
                grade = "D-"
            # E range
            elif (zScore > -2):
                grade = "E "
            # F range
            else:
                grade = "F "

            card["zScore"] = str(zScore)[:6]
            card["grade"] = grade

            print(card["grade"], card["zScore"], " ", card["GIH WR"], " ", card["Name"])
        else:
            print("Inadequate data for", card["Name"])
            print("  zscore  gihwr   name")
        jsonDataDict[card["Name"]] = card


# import fuzzywuzzy
from fuzzywuzzy import process

while True:
    delimiter = ";"  # the delimiter between every card

    # input card name(s) with a delimiter
    inputCards = input("Enter card name → ")
    cards = []
    # iterate through every character. if it isn't a space and it isn't the
    # delimiter, add it to the card string. if it's a space, don't do anything.
    # if it's the delimiter reset the card stringa nd append it to the cards.
    currentCardString = ""
    for char in inputCards:
        if not char == delimiter and not char == " ":
            currentCardString += char
        if char == delimiter:
            cards.append(currentCardString)
            currentCardString = ""
    cards.append(currentCardString)

    # print the table for every card
    print("   zscore   ohwr  gihwr   name")

    for card in cards:
        bestMatch = process.extractOne(card, cardNames)
        cardName = bestMatch[0]
        cardInDict = jsonDataDict[cardName]
        if (cardInDict["GIH WR"] and cardInDict["OH WR"]):
            print(cardInDict["grade"], cardInDict["zScore"], " ",
                  cardInDict["OH WR"], " ", cardInDict["GIH WR"], " ",
                  cardInDict["Name"])
        else:
            print("Insufficient data for", cardInDict["Name"])




