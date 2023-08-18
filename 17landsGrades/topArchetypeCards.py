import json

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

import ANSI
import os

# calculate the grade based on the z-score
def calculateGrade(zScore):
    result = "  "  # use this as extra spacing

    # Special: SS
    if zScore > 3.5:
        result = f"\033[38;2;250;250;255mSS{ANSI.reset}"
    # S range
    if zScore > (3.5 - 1 / 3):
        result = f"\033[38;2;250;250;254mS+{ANSI.reset}"
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


colorPairs = ["WU", "WB", "WR", "WG",
              "UB", "UR", "UG",
              "BR", "BG",
              "RG"]

import functools

numCards = 200
while numCards > 100:
    numCards = int(input("Please enter the number of cards you want to display for each archetype, not over 100. "))

for colorPair in colorPairs:
    print(f"\n🥏Color pair: {colorPair}")
    with open(f"cardRatingsAll/{colorPair}.json") as data:
        sortedCards = []
        jsonData = json.load(data)
        for cardName, cardData in jsonData["cardData"].items():
            if (cardData["# GIH"] > 100) and (cardData["Rarity"] == "common" or cardData["Rarity"] == "uncommon"):
                sortedCards.append(cardData)
        sortedCards = sorted(sortedCards,
                             key=functools.cmp_to_key(compareCards))

        for i in range(numCards):  # print 30 cards
            card = sortedCards[i]
            zScoreGIH = f"{card['zScoreGIH']:5}"
            zScoreOH = f"{card['zScoreOH']:5}"
            zScoreIWD = f"{card['zScoreIWD']:5}"

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
                f"{card['Name']}")


