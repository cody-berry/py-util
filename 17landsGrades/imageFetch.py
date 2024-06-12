# in cardRatingsAll/all.json, fetches all the URLs of the cards
# each card should be something like: {
# "Name": "Abuelo's Awakening",
# "Color": "W", "Rarity": "rare",
# "# GIH": 2399, "# GD": 1487,
# "# GNS": 3690, "# OH": 912,
# "url": "https://cards.scryfall.io/large/front/f/9/f93b725e-2b9c-4830-ac54-b2562afe09bb.jpg?1699043056",
# "OH WR": "45.7%", "GIH WR": "52.1%",
# "ATA": "6.13", "ALSA": "4.45", "IWD": "-2.37pp",
# "zScoreGIH": -0.93, "zScoreOH": -1.78, "zScoreIWD": -1.14}
# the url is what we want to find
import json
imageURLs = []
with open("./cardRatingsAll/all.json") as allDataWrapper:
    allData = json.load(allDataWrapper)
    cardData = allData["cardData"]
    for card in cardData.items():
        imageURLs.append([card[0], card[1]["url"]])


setName = "mh3"
import requests
for urlData in imageURLs:
    url = urlData[1]
    fileToSaveIn = f"./cardImages/mh3/{urlData[0]}.jpg"

    response = requests.get(url)

    if response.status_code == 200:
        with open(fileToSaveIn, "wb") as file:
            file.write(response.content)