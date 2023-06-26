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

# calculate the grade based on the z-score
def calculateGrade(zScore):
    result = "  "  # use this as extra spacing

    # S range
    if zScore > 3:
        result = "S+"
    elif zScore > 2.75:
        result = "S "
    elif zScore > 2.50:
        result = "S-"
    # A range
    elif zScore > (2.5 - 1 / 3):
        result = "A+"
    elif zScore > (1.5 + 1 / 3):
        result = "A "
    elif zScore > 1.5:
        result = "A-"
    # B range
    elif zScore > (1.5 - 1 / 3):
        result = "B+"
    elif zScore > (0.5 + 1 / 3):
        result = "B "
    elif zScore > 0.5:
        result = "B-"
    # C range
    elif zScore > (0.5 - 1 / 3):
        result = "C+"
    elif zScore > (-0.5 + 1 / 3):
        result = "C "
    elif zScore > -0.5:
        result = "C-"
    # D range
    elif zScore > (-0.5 - 1 / 3):
        result = "D+"
    elif zScore > (-1.5 + 1 / 3):
        result = "D "
    elif zScore > -1.5:
        result = "D-"
    # E range
    elif zScore > -2:
        result = "E "
    # F range
    else:
        result = "F "

    return result


# Opens the csv and puts it in a list dictionaries
import csv
import json

data = []

# utf-8 encoding without the byte order mark
# parse the csv data into a list of dictionaries for each card
with open("./cardRatings/card-ratings-2023-06-26.csv", "r",
          encoding="utf-8-sig") as csvData:
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
    meanGIH = 0
    meanOH = 0
    meanIWD = 0

    # new dataset needed to account for cards without enough data
    dataLength = 0
    for card in jsonData:
        if card["OH WR"] and card["IWD"]:
            meanGIH += float(card["GIH WR"][:-1])
            meanOH += float(card["OH WR"][:-1])
            meanIWD += float(card["IWD"][:-2])
            dataLength += 1
    meanGIH /= dataLength
    meanOH /= dataLength
    meanIWD /= dataLength

    # calculate the standard deviation
    stdevGIH = 0
    stdevOH = 0
    stdevIWD = 0
    for card in jsonData:
        if card["OH WR"] and card["IWD"]:
            stdevGIH += (float(card["GIH WR"][:-1]) - meanGIH) ** 2
            stdevOH += (float(card["OH WR"][:-1]) - meanOH) ** 2
            stdevIWD += (float(card["IWD"][:-2]) - meanIWD) ** 2
    stdevGIH /= dataLength
    stdevGIH **= 0.5
    stdevOH /= dataLength
    stdevOH **= 0.5
    stdevIWD /= dataLength
    stdevIWD **= 0.5

    print("Overall data:")
    print("GIH WR%           OH WR%            IWD                name")

    # print the card data
    for i in range(0, len(jsonData)):
        card = jsonData.pop()
        cardNames.append(card["Name"])
        if card["OH WR"] and card["IWD"]:
            # calculate and set zScores and grades for GIH WR% (game in hand
            # winrate), OH WR% (opening hand winrate), and IWD (improvement
            # when drawn).
            zScore = (float(card["GIH WR"][:-1]) - meanGIH) / stdevGIH

            grade = calculateGrade(zScore)

            card["zScoreGIH"] = str(zScore)[:6]
            card["gradeGIH"] = grade

            zScore = (float(card["OH WR"][:-1]) - meanOH) / stdevOH

            grade = calculateGrade(zScore)

            card["zScoreOH"] = str(zScore)[:6]
            card["gradeOH"] = grade

            zScore = (float(card["IWD"][:-2]) - meanIWD) / stdevIWD

            grade = calculateGrade(zScore)

            card["zScoreIWD"] = str(zScore)[:6]
            card["gradeIWD"] = grade

            # space properly so that if there is a negative in the IWD, it
            # doesn't matter even though a negative takes up a character
            if (float(card["IWD"][:-2]) > 0):
                print(card["gradeGIH"], card["zScoreGIH"], card["GIH WR"], " ",
                      card["gradeOH"], card["zScoreOH"], card["OH WR"], " ",
                      card["gradeIWD"], card["zScoreIWD"], card["IWD"], "  ",
                      card["Name"])
            else:
                print(card["gradeGIH"], card["zScoreGIH"], card["GIH WR"], " ",
                      card["gradeOH"], card["zScoreOH"], card["OH WR"], " ",
                      card["gradeIWD"], card["zScoreIWD"], card["IWD"], " ",
                      card["Name"])

        else:
            print("Inadequate data for", card["Name"])
            print("GIH WR%           OH WR%            IWD                name")
        jsonDataDict[card["Name"]] = card

# import fuzzywuzzy
from fuzzywuzzy import process

while True:
    delimiter = ";"  # the delimiter between every card

    # input card name(s) with a delimiter
    inputCards = input("Enter card name (input 'instruction' for instructions list)→ ")
    cards = []
    # iterate through every character. if it isn't a space and it isn't the
    # delimiter, add it to the card string. if it's a space, don't do anything.
    # if it's the delimiter reset the card string and append it to the cards.
    currentCardString = ""
    for char in inputCards:
        if not char == delimiter and not char == " ":
            currentCardString += char
        if char == delimiter:
            cards.append(currentCardString)
            currentCardString = ""
    cards.append(currentCardString)

    # show oracle text if there is only one card and the first is exclamation
    showOracleText = False
    if len(cards) == 1:
        if currentCardString[0] == "!":
            showOracleText = True
            cards = [cards[0][1:]]

    # show an instruction manual if "instruction" is the input
    if len(cards) == 1:
        if currentCardString == "instruction":
            print("Instruction manual:")
            print("⚠ Please do not press Enter without anything inside. ⚠")
            print("At the top of the print line, you will see the ratings of "
                  + "all cards, formatted as the last part says.")
            print("Type a number of cards. You can use abbreviations and you "
                  + "can get away with most typos. Be careful, though. Don't "
                  + "expect to get what you want, especially if the input is "
                  + "part of another card.")
            print("Card names are split with ';'. ")
            print("Spaces don't matter. ")
            print("Don't use ';' as an ender.")
            print("Card data is in the format of:")
            print("{grade for GIH WR} {zScore for GIH WR} {GIH WR} {repeat for "
                  + "OH WR and IWD} {card name}")
            print("Where:")
            print("— GIH WR is the winrate when the card is in your hand. ")
            print("— OH WR is the winrate when the card is in your opening hand.")
            print("— IWD is the improvement when drawn.")
            print("— The grade ranges from S+, S, S-, all the way down to D-, E, "
                  + "and F. ")
            print("— The z-score is the number of standard deviations away from"
                  + "the mean that whatever you're measuring the z-score of is.")
            print("— If you type '!' as the first character and there are no ';"
                  + "'s, it will show the oracle text.")

    else:
        # print the table for every card
        print("GIH WR%           OH WR%            IWD                name")

        for card in cards:
            bestMatch = process.extractOne(card, cardNames)
            cardName = bestMatch[0]
            cardInDict = jsonDataDict[cardName]
            if (cardInDict["GIH WR"] and cardInDict["OH WR"]):
                # space properly so that if there is a negative in the IWD, it
                # doesn't matter even though a negative takes up a character
                if (float(cardInDict["IWD"][:-2]) > 0):
                    print(cardInDict["gradeGIH"], cardInDict["zScoreGIH"], cardInDict["GIH WR"], " ",
                          cardInDict["gradeOH"], cardInDict["zScoreOH"], cardInDict["OH WR"], " ",
                          cardInDict["gradeIWD"], cardInDict["zScoreIWD"], cardInDict["IWD"], "  ",
                          cardInDict["Name"])
                else:
                    print(cardInDict["gradeGIH"], cardInDict["zScoreGIH"], cardInDict["GIH WR"], " ",
                          cardInDict["gradeOH"], cardInDict["zScoreOH"], cardInDict["OH WR"], " ",
                          cardInDict["gradeIWD"], cardInDict["zScoreIWD"], cardInDict["IWD"], " ",
                          cardInDict["Name"])
            else:
                print("Insufficient data for", cardInDict["Name"])
                print("GIH WR%           OH WR%            IWD                name")
            if showOracleText:
                print("There is no oracle text available in the card ratings.")

