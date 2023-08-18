import json

# define the amount of diff between the second highest zScore and the highest
# zScore to make it a secret gold card.
minDiff = 0
while not minDiff:
    try:
        minDiff = float(input("Enter the maximum diff between the highest z-score and the other color pairs."))
    except:
        pass

# open the master json for all
with open("cardRatingsAll/master.json") as master:
    # iterate through each element of the json. card name and card data.
    masterJSON = json.load(master)
    for cardName, cardData in masterJSON.items():
        # if it's monocolored or colorless...
        if 0 <= len(cardData["color"]) <= 1:
            # define the highest and second highest z-score GIH, along with the
            # one that has the highest z-score in GIH. they start at -10, a
            # z-score that no card has.
            highestZScore = -10
            secondHighestZScore = -10
            highestZScoreColorPair = ""

            # iterate through each color pair.
            for colorPair in [
                "WU", "WB", "WR", "WG",
                "UB", "UR", "UG",
                "BR", "BG", "RG"
            ]:
                colorPairStats = cardData[colorPair]
                # if it has more than 100 # GIH...
                if colorPairStats["# GIH"] > 100:
                    # if it's more than the highest z-score...
                    if colorPairStats["zScoreGIH"] > highestZScore:
                        # make the second highest z-score the currently highest
                        # z-score.
                        secondHighestZScore = highestZScore

                        # define the color pair that has this.
                        highestZScoreColorPair = colorPair

                        # make the highest z-score this z-score.
                        highestZScore = colorPairStats["zScoreGIH"]

                    # otherwise, if it's more than the second-to-highest z-score...
                    elif colorPairStats["zScoreGIH"] > secondHighestZScore:
                        # make the second highest z-score this z-score.
                        secondHighestZScore = colorPairStats["zScoreGIH"]

            # if the second highest z-score GIH is above -10...
            if secondHighestZScore > -10:
                # if the difference between the highest z-score and the second
                # highest z-score GIH is above minDiff...
                if (highestZScore - secondHighestZScore) > minDiff:
                    # say that this card is a secret golden card with the
                    # highest color pair.
                    print(f"{cardName} is a secret {highestZScoreColorPair} card!")








