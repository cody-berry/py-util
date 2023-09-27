import json

# define the amount of diff between the top zScore and the all zScore
# to make it a secret top card.
minDiff = 0
while minDiff <= 0:
    try:
        minDiff = float(input(
            "Enter the maximum diff between the highest z-score and the other color pairs."))
    except:
        print("Please enter an integer. ")
        pass

# open the master json for all and top
with open("cardRatingsTop/master.json") as top:
    with open("cardRatingsAll/master.json") as all:
        # iterate through each element of the json for each color pair.
        allJSON = json.load(all)
        topJSON = json.load(top)
        colorPairs = [
            "WU", "WB", "WR", "WG",
            "UB", "UR", "UG",
            "BR", "BG",
            "RG", "all"
        ]
        for colorPair in colorPairs:
            print(f"🥏 {colorPair}")
            for cardName, allCardData in allJSON.items():
                # get the GIH WR% zScore for the card in "all"
                allZScore = allCardData[colorPair]["zScoreGIH"]

                # get the GIH WR% zScore for the card in "top"
                topZScore = topJSON[cardName][colorPair]["zScoreGIH"]

                # if the top zScore is minDiff or more higher than the all zScore,
                # say that the card is a secret top player card
                if (topZScore - allZScore) > minDiff:
                    # say that this card is a secret golden card with the
                    # highest color pair.
                    print(
                        f"{cardName} is a secret top player card!")
            print("\n")








