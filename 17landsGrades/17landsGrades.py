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

    # Special: SS
    if zScore > 3.5:
        result = "SS"
    # S range
    if zScore > (3.5 - 1 / 3):
        result = "S+"
    elif zScore > (2.5 + 1 / 3):
        result = "S "
    elif zScore > 2.5:
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


import json
meanGIH = 0
meanOH = 0
meanIWD = 0
stdevGIH = 0
stdevOH = 0
stdevIWD = 0

# print the name and game in hand win rate of each card
with open("./cardRatingsAuto/all.json", "r") as jsonFile:
    print(jsonFile)
    jsonData = json.load(jsonFile)
    cardData = jsonData["cardData"]

    # calculate the mean
    meanGIH = jsonData["generalStats"]["OH WR"]["μ"]
    meanOH = jsonData["generalStats"]["GIH WR"]["μ"]
    meanIWD = jsonData["generalStats"]["IWD"]["μ"]

    # calculate the standard deviation
    stdevGIH = jsonData["generalStats"]["OH WR"]["σ"]
    stdevOH = jsonData["generalStats"]["GIH WR"]["σ"]
    stdevIWD = jsonData["generalStats"]["IWD"]["σ"]

    print("Overall data:")
    print("GIH WR%           OH WR%            IWD                name")

    # print the card data
    for cardName, card in cardData.items():
        if card["OH WR"] and card["IWD"]:
            # calculate and set zScores and grades for GIH WR% (game in hand
            # winrate), OH WR% (opening hand winrate), and IWD (improvement
            # when drawn).
            zScoreGIH = (float(card["GIH WR"][:-1]) - meanGIH) / stdevGIH

            gradeGIH = calculateGrade(zScoreGIH)

            zScoreOH = (float(card["OH WR"][:-1]) - meanOH) / stdevOH

            gradeOH = calculateGrade(zScoreOH)

            zScoreIWD = (float(card["IWD"][:-2]) - meanIWD) / stdevIWD

            gradeIWD = calculateGrade(zScoreIWD)

            # space properly so that if there is a negative in the IWD, it
            # doesn't matter even though a negative takes up a character
            if (float(card["IWD"][:-2]) > 0):
                print(gradeGIH, card["zScoreGIH"], card["GIH WR"], " ",
                      gradeOH, card["zScoreOH"], card["OH WR"], " ",
                      gradeIWD, card["zScoreIWD"], card["IWD"], "  ",
                      card["Name"])
            else:
                print(gradeGIH, zScoreGIH, card["GIH WR"], " ",
                      gradeOH, zScoreOH, card["OH WR"], " ",
                      gradeIWD, zScoreIWD, card["IWD"], " ",
                      card["Name"])

        else:
            print("Inadequate data for", card["Name"])
            print("GIH WR%           OH WR%            IWD                name")

    cardNames = list(cardData.keys())

# import the set data
import requests

# constructing the API request
set_code = "ltr"
url = f"https://api.scryfall.com/cards/search?q=set:{set_code}"

# sending the API request
response = requests.get(url)

scryfallDict = {}

# processing the API response
if response.status_code == 200:
    data = response.json()
    # extracting relevant information from the response
    cards = data['data']

    # saving the data
    # using pagination to retrieve all the cards
    while data["has_more"]:
        next_page_url = data["next_page"]
        response = requests.get(next_page_url)
        if (response.status_code == 200):
            data = response.json()
            cards.extend(data['data'])
        else:
            raise FileNotFoundError(f"Could not load next page. Error code: {response.status_code}")

    # transform the json list into a json dict
    scryfallDict = {card["name"]: card for card in cards}
    print("Data saved successfully.")
else:
    raise FileNotFoundError(f"Could not load scryfall data for {set_code}. Error code: {response.status_code}")


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
            print("⚠ Please forgive any typos, as this was made in half a month or so. ⚠")
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

        # print the table for every card
        print("GIH WR%           OH WR%            IWD                name")

    # no matter how many cards there are, if the third character is ":",
    # set the color pair to the combination of the first and second
    # chars if it's in WU, UB, BR, RG, GW, WR, RU, UG, GB, and BW.
    # otherwise, set the color pair to "all".
    colorPair = "all"
    if inputCards[2] == ":":
        if inputCards[:2] in ["WU", "UB", "BR", "RG", "WG",
                              "WR", "UR", "UG", "BG", "WB"]:
            colorPair = inputCards[:2]

    # gather all the cards so that we can sort them
    cardsSelected = []
    with open(f"cardRatingsAuto/{colorPair}.json", "r") as data:
        data = json.load(data)
        for card in cards:
            bestMatch = process.extractOne(card, cardNames)
            cardName = bestMatch[0]
            card = data[cardName]
            cardsSelected.append(card)

    # sort the cards by gih wr% by importing functools, making a
    # compare function, and then sorting using that.
    import functools

    def compareCards(card1, card2):
        # handles ever in hand winrate
        if float(card1["GIH WR"][:-1]) > float(card2["GIH WR"][:-1]):
            return -1
        if float(card1["GIH WR"][:-1]) < float(card2["GIH WR"][:-1]):
            return 1
        else:
            # handles opening hand winrate
            if float(card1["OH WR"][:-1]) > float(card2["OH WR"][:-1]):
                return -1
            if float(card1["OH WR"][:-1]) < float(card2["OH WR"][:-1]):
                return 1
            else:
                # handles improvement when drawn
                if float(card1["IWD"][:-2]) > float(card2["IWD"][:-2]):
                    return -1
                if float(card1["IWD"][:-2]) < float(card2["IWD"][:-2]):
                    return 1
                else:
                    # if all are the same, maintain the order
                    return 0

    sortedCards = sorted(cardsSelected, key=functools.cmp_to_key(compareCards))
    for card in sortedCards:
        print("🍓")
        print(card["Name"])

    for card in sortedCards:
        cardName = card["Name"]
        if card["GIH WR"] and card["OH WR"]:
            # space properly so that if there is a negative in the IWD, it
            # doesn't matter even though a negative takes up a character
            if float(card["IWD"][:-2]) > 0:
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
            print("Insufficient data for", card["Name"])
            print("GIH WR%           OH WR%            IWD                name")
        if showOracleText:
            # show all relevant information
            scryfallCardData = scryfallDict[cardName]
            print(f"\n{cardName} {scryfallCardData['mana_cost']}")
            print(scryfallCardData["type_line"])
            print(scryfallCardData["oracle_text"])

