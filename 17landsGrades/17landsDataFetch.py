# ⚠Only run once a day if you don't want 17lands to complain at you.⚠
import requests


def fetchData(url):
    response = requests.get(url)

    # checks if the data is valid or not (200 is a successful status code)
    if response.status_code == 200:
        data = response.json()
        print("Data successfully loaded")
        return data
    else:
        # if not, print that it failed to fetch data
        print("Failed to fetch data. Error code", response.status_code)
        return None


# the url that handles the expansion for the current set
baseURL = (f'https://www.17lands.com/card_ratings/data?expansion=LTR'
              '&format=PremierDraft'
              '&start_date=2023-05-28'
              '&end_date=2023-07-06')
print(baseURL)


# transforms data like: {
# 'seen_count': 133247,
# 'avg_seen': 5.155973492836612,
# 'pick_count': 18055,
# 'avg_pick': 7.534865688175021,
# 'game_count': 64577,
# 'win_rate': 0.5349427814856683,
# 'sideboard_game_count': 41751,
# 'sideboard_win_rate': 0.5578549016790016,
# 'opening_hand_game_count': 10224,
# 'opening_hand_win_rate': 0.5102699530516432,
# 'drawn_game_count': 17519,
# 'drawn_win_rate': 0.5682972772418518,
# 'ever_drawn_game_count': 27743,
# 'ever_drawn_win_rate': 0.5469127347438993,
# 'never_drawn_game_count': 36894,
# 'never_drawn_win_rate': 0.5268336314847942,
# 'drawn_improvement_win_rate': 0.020079103259105113,
# 'name': 'Banish from Edoras',
# 'color': 'W',
# 'rarity': 'common',
# 'url': 'https://cards.scryfall.io/border_crop/front/a/4/a4410076-e1fe-45f3-a0ca-a91ab0133ff4.jpg?1686397326',
# 'url_back': '',
# 'types': ['Sorcery']
# } into data like this: {
# "Name": "Banish from Edoras",
# "Color": "W",
# "Rarity": "C",
# "ALSA": "5.16",
# "ATA": "7.53",
# "OH WR": "51.0%",
# "# GIH": "27743",
# "GIH WR": "54.7%",
# "IWD": "2.0pp"
# }
def processData(data):
    result = []
    for card in data:
        cardAlternate = {}
        cardAlternate["Name"] = card["name"]
        cardAlternate["Color"] = card["color"]
        cardAlternate["Rarity"] = card["rarity"]
        cardAlternate["OH WR"] = ""
        cardAlternate["GIH WR"] = ""
        cardAlternate["ATA"] = ""
        cardAlternate["ALSA"] = ""
        cardAlternate["IWD"] = ""

        # round to 2 decimal points for ALSA and ATA
        # only account if stat exists
        if (card["avg_seen"]):
            cardAlternate["ALSA"] = str(round(card["avg_seen"], 2))
        if (card["avg_pick"]):
            cardAlternate["ATA"] = str(round(card["avg_pick"], 2))

        # round to 1 decimal point for OH WR and GIH
        # WR and add %
        if (card["opening_hand_win_rate"]):
            cardAlternate["OH WR"] = str(round(card["opening_hand_win_rate"]*100, 1)) + "%"
        if (card["ever_drawn_win_rate"]):
            cardAlternate["GIH WR"] = str(round(card["ever_drawn_win_rate"]*100, 1)) + "%"

        # round to 1 decimal point for IWD and add
        # pp
        if (card["drawn_improvement_win_rate"]):
            cardAlternate["IWD"] = str(round(card["drawn_improvement_win_rate"]*100, 1)) + "pp"
        result.append(cardAlternate)
    return str(result)


with open("cardRatingsAuto/all.json", "w") as cardDataJSON:
    data = fetchData(baseURL)
    cardDataJSON.write(processData(data))

# the additions list is a list of strings to add to the url. the base url
# is handled first.
additions = ["&colors=WU", "&colors=WB", "&colors=WR", "&colors=WG",
             # W color pairs
             "&colors=UB", "&colors=UR", "&colors=UG",  # U color pairs
             "&colors=BR", "&colors=BG",  # B color pairs
             "&colors=RG"  # R color pairs
             ]

for addition in additions:
    totalURL = baseURL + addition
    print(totalURL)
    # print color pair:
    colorPair = addition[-2:]
    print(colorPair)

    with open(f"cardRatingsAuto/{colorPair}.json", "w") as cardDataJSON:
        data = fetchData(totalURL)
        cardDataJSON.write(processData(data))



