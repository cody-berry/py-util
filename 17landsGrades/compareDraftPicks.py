import datetime

# Testing section

# Section 1: Testing mean on a distribution.
# import numpy as np


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

import ANSI


# calculate the grade based on the z-score
def calculateGrade(zScore):
    result = "  "  # use this as extra spacing

    # Special: SS
    if zScore > 3.5:
        result = f"\033[38;2;255;255;255mSS{ANSI.reset}"
    # S range
    if zScore > (3.5 - 1 / 3):
        result = f"\033[38;2;254;254;254mS+{ANSI.reset}"
    elif zScore > (2.5 + 1 / 3):
        result = f"\033[38;2;244;244;244mS {ANSI.reset}"
    elif zScore > 2.5:
        result = f"\033[38;2;234;234;234mS-{ANSI.reset}"
    # A range
    elif zScore > (2.5 - 1 / 3):
        result = f"\033[38;2;223;223;223mA+{ANSI.reset}"
    elif zScore > (1.5 + 1 / 3):
        result = f"\033[38;2;220;220;220mA {ANSI.reset}"
    elif zScore > 1.5:
        result = f"\033[38;2;217;217;217mA-{ANSI.reset}"
    # B range
    elif zScore > (1.5 - 1 / 3):
        result = f"\033[38;2;214;214;214mB+{ANSI.reset}"
    elif zScore > (0.5 + 1 / 3):
        result = f"\033[38;2;211;211;211mB {ANSI.reset}"
    elif zScore > 0.5:
        result = f"\033[38;2;200;200;200mB-{ANSI.reset}"
    # C range
    elif zScore > (0.5 - 1 / 3):
        result = f"\033[38;2;182;182;182mC+{ANSI.reset}"
    elif zScore > (-0.5 + 1 / 3):
        result = f"\033[38;2;152;152;152mC {ANSI.reset}"
    elif zScore > -0.5:
        result = f"\033[38;2;142;142;142mC-{ANSI.reset}"
    # D range
    elif zScore > (-0.5 - 1 / 3):
        result = f"\033[38;2;131;131;131mD+{ANSI.reset}"
    elif zScore > (-1.5 + 1 / 3):
        result = f"\033[38;2;117;117;117mD {ANSI.reset}"
    elif zScore > -1.5:
        result = f"\033[38;2;104;104;104mD-{ANSI.reset}"
    # E range
    elif zScore > -2:
        result = f"\033[38;2;90;90;90mE {ANSI.reset}"
    # F range
    else:
        result = f"\033[38;2;75;75;75mF {ANSI.reset}"

    return result


# pads a string with 0s to the right until it reaches the length. it shortens
# the string if it is too long.
def padEnd(string, length):
    if len(string) < length:
        return string + "0" * (length - len(string))
    else:
        return string[:length]


import json

meanGIH = 0
meanOH = 0
meanIWD = 0
stdevGIH = 0
stdevOH = 0
stdevIWD = 0

# print the name and game in hand win rate of each card
with open("cardRatingsAll/all.json", "r") as jsonFile:
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

    print(f"     {ANSI.dimWhite}n{ANSI.reset} {ANSI.dimWhite}|{ANSI.reset} "
          f"GIH WR%         {ANSI.dimWhite}|{ANSI.reset} "
          f"OH WR%          {ANSI.dimWhite}|{ANSI.reset} "
          f"IWD                {ANSI.dimWhite}|{ANSI.reset} "
          f"name")

    # print the card data
    for cardName, card in cardData.items():
        if card["# GIH"] > 100:
            # calculate and set zScores and grades for GIH WR% (game in hand
            # winrate), OH WR% (opening hand winrate), and IWD (improvement
            # when drawn).
            zScoreGIH = padEnd(str(card["zScoreGIH"]), 5)
            zScoreOH = padEnd(str(card["zScoreOH"]), 5)
            zScoreIWD = padEnd(str(card["zScoreIWD"]), 5)

            gradeGIH = calculateGrade(float(card["zScoreGIH"]))

            gradeOH = calculateGrade(float(card["zScoreOH"]))

            gradeIWD = calculateGrade(float(card["zScoreIWD"]))

            print(
                f"{ANSI.dimWhite}{card['# GIH']:>6}{ANSI.reset} "  # sample size
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeGIH} {ANSI.dimWhite}{float(zScoreGIH): 6.3f}{ANSI.reset} {card['GIH WR']} "
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeIWD} {ANSI.dimWhite}{float(zScoreOH): 6.3f}{ANSI.reset} {card['OH WR']} "
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeOH} {ANSI.dimWhite}{float(zScoreIWD): 6.3f}{ANSI.reset} {float(card['IWD'][:-2]): >6.2f}{ANSI.dimWhite}pp{ANSI.reset} "
                f"{ANSI.dimWhite}|{ANSI.reset} {card['Name']}")

        else:
            print(f"Inadequ{ANSI.dimWhite}|{ANSI.reset}te data for", card["Name"])
            print(f"     {ANSI.dimWhite}n{ANSI.reset} {ANSI.dimWhite}|{ANSI.reset} "
                  f"GIH WR%         {ANSI.dimWhite}|{ANSI.reset} "
                  f"OH WR%          {ANSI.dimWhite}|{ANSI.reset} "
                  f"IWD                {ANSI.dimWhite}|{ANSI.reset} "
                  f"name")

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
            raise FileNotFoundError(
                f"Could not load next page. Error code: {response.status_code}")

    # transform the json list into a json dict
    scryfallDict = {card["name"]: card for card in cards}
    print("Data saved successfully.")
else:
    raise FileNotFoundError(
        f"Could not load scryfall data for {set_code}. Error code: {response.status_code}")

# import fuzzywuzzy
from fuzzywuzzy import process

previousUserInput = ""

# get the time since the top data and normal data was last updated

# use a function to format a time difference into something like "over a year
# ago" or "within a minute ago"
def format_time_difference(time_difference):

    # get the number of seconds, days, hours, and minutes ago
    days = time_difference.days
    seconds = time_difference.seconds
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    string = ""
    # if years > 1:
    #     return "Over 2 years ago"
    # if years > 0:
    #     return "A year ago" if months == 0 else f"A year and {months} month{'s' if months > 1 else ''} ago"
    # if months > 0:
    #     return "A month ago" if months == 1 else f"{months} months ago"
    if days > 0:
        string = "a day " if days == 1 else f"{days} days "
    if hours > 0:
        if string:
            string += "and "
        string += "an hour " if hours == 1 else f"{hours} hours "
    if minutes > 1 and days == 0:
        if string:
            string += "and "
        string += f"{minutes} minutes "
    if minutes == 1 and hours == 0 and days == 0:
        string = "a minute and 1 second " if seconds == 1 else f"a minute and {seconds} seconds "
    if minutes == 0:
        return "within a minute ago"
    return string + "ago"

currentTime = datetime.datetime.now()

# read the last updated time for cardRatingsAll and cardRatingsTop.
with open("cardRatingsAll/lastUpdated.json", "r") as lastUpdated:
    lastUpdatedList = json.loads(lastUpdated.readline())
    lastUpdatedTime = datetime.datetime(
        lastUpdatedList[0],  # years
        lastUpdatedList[1],  # months
        lastUpdatedList[2],  # days
        lastUpdatedList[3],  # hours
        lastUpdatedList[4],  # minutes
        lastUpdatedList[5]   # seconds
    )
    print(f"Updated cardRatingsAll {format_time_difference(currentTime - lastUpdatedTime)}")

with open("cardRatingsTop/lastUpdated.json", "r") as lastUpdated:
    lastUpdatedList = json.loads(lastUpdated.readline())
    lastUpdatedTime = datetime.datetime(
        lastUpdatedList[0],  # years
        lastUpdatedList[1],  # months
        lastUpdatedList[2],  # days
        lastUpdatedList[3],  # hours
        lastUpdatedList[4],  # minutes
        lastUpdatedList[5]   # seconds
    )
    print(f"Updated cardRatingsTop {format_time_difference(currentTime - lastUpdatedTime)}")

while True:
    delimiter = ","  # the delimiter between every card

    # input card name(s) with a delimiter
    inputCards = input(
        "Enter card name (input 'instruction' for instructions list)→ ")

    if inputCards == "exit":
        print("Exitting!...")
        break

    # no matter how many cards there are, if the third character is ":",
    # set the color pair to the combination of the first and second
    # chars if it's in WU, UB, BR, RG, GW, WR, RU, UG, GB, and BW.
    # otherwise, set the color pair to "all".
    colorPair = "all"
    if inputCards and inputCards[2] == ":":
        if inputCards[:2].upper() in ["WU", "UB", "BR", "RG", "WG",
                                      "WR", "UR", "UG", "BG", "WB"]:
            colorPair = inputCards[:2].upper()
            inputCards = inputCards[3:]
    # if inputCards is empty, set it to the previous user input, but add/remove
    # a ~ if necessary.
    if inputCards == "" or inputCards == " ":
        inputCards = previousUserInput

        if colorPair == "all":  # only if the color pair wasn't selected
            if inputCards and inputCards[2] == ":":
                if inputCards[:2].upper() in ["WU", "UB", "BR", "RG", "WG",
                                              "WR", "UR", "UG", "BG", "WB"]:
                    colorPair = inputCards[:2].upper()
                    inputCards = inputCards[3:]
                    print(f"🌈Color filter: {colorPair}")
            if inputCards[0] == '~':
                inputCards = inputCards[1:]
            else:
                inputCards = f"~{inputCards}"
        else:
            # otherwise, trim any residual color pair
            if inputCards and inputCards[2] == ":":
                if inputCards[:2].upper() in ["WU", "UB", "BR", "RG", "WG",
                                              "WR", "UR", "UG", "BG", "WB"]:
                    inputCards = inputCards[3:]

    # set the previous user input to inputCards.
    # if the color pair was set, then there will be an unnecessary residual
    # {colorPair}:
    previousUserInput = inputCards
    if previousUserInput and previousUserInput[2] == ":" and colorPair != "all":
        if previousUserInput[:2].upper() in ["WU", "UB", "BR", "RG", "WG",
                                             "WR", "UR", "UG", "BG", "WB"]:
            previousUserInput = previousUserInput[3:]
    if colorPair != "all":
        previousUserInput = f"{colorPair}:{previousUserInput}"

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
            print(
                "— OH WR is the winrate when the card is in your opening hand.")
            print("— IWD is the improvement when drawn.")
            print(
                "— The grade ranges from S+, S, S-, all the way down to D-, E, "
                + "and F. ")
            print("— The z-score is the number of standard deviations away from"
                  + "the mean that whatever you're measuring the z-score of is.")
            print("— If you type '!' as the first character and there are no ';"
                  + "'s, it will show the oracle text.")

    # no matter how many cards there are, if the first character is "~",
    # set the players to top. otherwise, set it to all.
    playerGroup = "All"
    if inputCards[0] == "~":
        playerGroup = "Top"

    print(f"{ANSI.dimWhite}[DATASET]{ANSI.reset} {playerGroup.lower()}")



    # gather all the cards so that we can sort them
    cardsSelected = []

    singleCard = False

    with open(f"cardRatings{playerGroup}/master.json", "r") as data:
        data = json.load(data)
        if (len(cards) == 1) and (colorPair == "all"):
            cardName = process.extractOne(cards[0], cardNames)[0]
            singleCard = True
            for colorPair in ['WU', 'UB', 'BR', 'RG', 'WG',
                              'WR', 'UR', 'UG', 'BG', 'WB']:
                card = data[cardName][colorPair]
                card["colorPair"] = colorPair
                card["Name"] = cardName
                cardsSelected.append(card)
        else:
            for card in cards:
                bestMatch = process.extractOne(card, cardNames)
                cardName = bestMatch[0]
                card = data[cardName][colorPair]
                card["Name"] = cardName
                cardsSelected.append(card)

    # sort the cards by gih wr% by importing functools, making a
    # compare function, and then sorting using that.
    import functools


    def compareCards(card1, card2):
        # handles not enough sample size
        if card1["# GIH"] < 100 or card2["# GIH"] < 100:
            return 0

        # handles ever in hand winrate
        if card1["zScoreGIH"] > card2["zScoreGIH"]:
            return -1
        if card1["zScoreGIH"] < card2["zScoreGIH"]:
            return 1
        else:
            # handles opening hand winrate
            if card1["zScoreOH"] > card2["zScoreOH"]:
                return -1
            if card1["zScoreOH"] < card2["zScoreOH"]:
                return 1
            else:
                # handles improvement when drawn
                if card1["zScoreIWD"] > card2["zScoreIWD"]:
                    return -1
                if card1["zScoreIWD"] < card2["zScoreIWD"]:
                    return 1
                else:
                    # if all are the same, maintain the order
                    return 0


    sortedCards = sorted(cardsSelected, key=functools.cmp_to_key(compareCards))
    if singleCard:
        print(
            f"🍓 {ANSI.blue}{cardName}{ANSI.reset} → ALSA {data[cardName]['ALSA']:0<4}"
            )
    else:
        print("🍓")
        for card in sortedCards:
            print(f"{ANSI.blue}{card['Name']}{ANSI.reset} → ALSA {data[card['Name']]['ALSA']:0<4}")

    # print the table for every card
    print(f"     {ANSI.dimWhite}n{ANSI.reset} {ANSI.dimWhite}|{ANSI.reset} "
          f"GIH WR%         {ANSI.dimWhite}|{ANSI.reset} "
          f"OH WR%          {ANSI.dimWhite}|{ANSI.reset} "
          f"IWD                {ANSI.dimWhite}|{ANSI.reset} "
          f"{'color pair' if singleCard else 'name'}")


    for card in sortedCards:
        if (card["# GIH"] > 100):
            # calculate and set zScores and grades for GIH WR% (game in hand
            # winrate), OH WR% (opening hand winrate), and IWD (improvement
            # when drawn).
            zScoreGIH = padEnd(str(card["zScoreGIH"]), 5)
            zScoreOH = padEnd(str(card["zScoreOH"]), 5)
            zScoreIWD = padEnd(str(card["zScoreIWD"]), 5)

            gradeGIH = calculateGrade(float(zScoreGIH))

            gradeOH = calculateGrade(float(zScoreOH))

            gradeIWD = calculateGrade(float(zScoreIWD))

            print(
                f"{ANSI.dimWhite}{card['# GIH']:>6}{ANSI.reset} "  # sample size
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeGIH} {ANSI.dimWhite}{float(zScoreGIH): 6.3f}{ANSI.reset} {card['GIH WR']} "
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeIWD} {ANSI.dimWhite}{float(zScoreOH): 6.3f}{ANSI.reset} {card['OH WR']} "
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{gradeOH} {ANSI.dimWhite}{float(zScoreIWD): 6.3f}{ANSI.reset} {float(card['IWD'][:-2]): >6.2f}{ANSI.dimWhite}pp{ANSI.reset} "
                f"{ANSI.dimWhite}|{ANSI.reset} "
                f"{card['colorPair'] if singleCard else card['Name']}")

        else:
            if not singleCard:
                print(f"Inadequ{ANSI.dimWhite}|{ANSI.reset}te data for", card["Name"])
                print(f"     {ANSI.dimWhite}n{ANSI.reset} {ANSI.dimWhite}|{ANSI.reset} "
                      f"GIH WR%         {ANSI.dimWhite}|{ANSI.reset} "
                      f"OH WR%          {ANSI.dimWhite}|{ANSI.reset} "
                      f"IWD                {ANSI.dimWhite}|{ANSI.reset} "
                      f"name")


    if showOracleText:
        # show all relevant information
        scryfallCardData = scryfallDict[cardName]
        print(f"\n{cardName} {scryfallCardData['mana_cost']}")
        print(scryfallCardData["type_line"])
        print(scryfallCardData["oracle_text"])
        print("")  # newline
