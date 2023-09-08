# ⚠Only run once a day if you don't want 17lands to complain at you.⚠
import json
import requests
import datetime

current_time = datetime.datetime.now() # extract the current time and save it

with open("cardRatingsTop/lastUpdated.json", "w") as lastUpdatedFile:
    lastUpdatedFile.write(
        str([current_time.year,
             current_time.month,
             current_time.day,
             current_time.hour,
             current_time.minute,
             current_time.second,
             current_time.microsecond])
    )


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
           '&format=PremierDraft&user_group=top')
baseURLBonusSheet = (f'https://www.17lands.com/card_ratings/data?expansion=WOT'
                     f'&format=PremierDraft&user_group=top')
bonusSheetToggle = True
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
# "GD WR": "54.7%",
# "IWD": "2.0pp"
# }
def processData(data):
    result = {}

    cardData = {}
    # make the OH WR and GIH WR mean so that we can keep
    # track
    OH_WRs = []
    GIH_WRs = []
    IWDs = []
    for card in data:
        cardAlternate = {}
        cardAlternate["Name"] = card["name"]
        cardAlternate["Color"] = card["color"]
        cardAlternate["Rarity"] = card["rarity"]
        cardAlternate["# GIH"] = card["ever_drawn_game_count"]
        cardAlternate["# GD"] = card["drawn_game_count"]
        cardAlternate["# GNS"] = card["never_drawn_game_count"]
        cardAlternate["# OH"] = card["opening_hand_game_count"]
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
            cardAlternate["OH WR"] = str(
                round(card["opening_hand_win_rate"] * 100, 1)) + "%"
            OH_WRs.append(float(cardAlternate["OH WR"][:-1]))
        if (card["drawn_win_rate"]):
            cardAlternate["GIH WR"] = str(
                round(card["drawn_win_rate"] * 100, 1)) + "%"
            GIH_WRs.append(float(cardAlternate["GIH WR"][:-1]))

        # round to 1 decimal point for IWD and add
        # pp
        if (card["drawn_improvement_win_rate"]):
            cardAlternate["IWD"] = str(
                round(card["drawn_improvement_win_rate"] * 100, 2)) + "pp"
            IWDs.append(float(cardAlternate["IWD"][:-2]))
        cardData[card["name"]] = cardAlternate

    # calculate the means (μ) and standard deviations (σ)
    OH_WRμ = 0
    for sample in OH_WRs:
        OH_WRμ += sample
    try:
        OH_WRμ /= len(OH_WRs)
    except ZeroDivisionError:
        OH_WRμ = 0
    GIH_WRμ = 0
    for sample in GIH_WRs:
        GIH_WRμ += sample
    try:
        GIH_WRμ /= len(GIH_WRs)
    except ZeroDivisionError:
        GIH_WRμ = 0
    IWDμ = 0
    for sample in IWDs:
        IWDμ += sample
    try:
        IWDμ /= len(IWDs)
    except ZeroDivisionError:
        IWDμ = 0

    OH_WRσ = 0
    for sample in OH_WRs:
        OH_WRσ += (sample - OH_WRμ) ** 2
    try:
        OH_WRσ /= len(OH_WRs)
        OH_WRσ **= 0.5
    except ZeroDivisionError:
        OH_WRσ = 0
    GIH_WRσ = 0
    for sample in GIH_WRs:
        GIH_WRσ += (sample - GIH_WRμ) ** 2
    try:
        GIH_WRσ /= len(GIH_WRs)
        GIH_WRσ **= 0.5
    except ZeroDivisionError:
        GIH_WRσ = 0
    IWDσ = 0
    for sample in IWDs:
        IWDσ += (sample - IWDμ) ** 2
    try:
        IWDσ /= len(IWDs)
        IWDσ **= 0.5
    except ZeroDivisionError:
        IWDσ = 0

    OH_WRStats = {"μ": OH_WRμ, "σ": OH_WRσ}
    GIH_WRStats = {"μ": GIH_WRμ, "σ": GIH_WRσ}
    IWDStats = {"μ": IWDμ, "σ": IWDσ}

    for cardName, card in cardData.items():
        cardData[cardName]["zScoreGIH"] = 0
        cardData[cardName]["zScoreOH"] = 0
        cardData[cardName]["zScoreIWD"] = 0
        if card["GIH WR"]:
            cardData[cardName]["zScoreGIH"] = (float(card["GIH WR"][:-1]) - GIH_WRμ)/GIH_WRσ
            cardData[cardName]["zScoreGIH"] = float(str(cardData[cardName]["zScoreGIH"])[:5])
        if card["OH WR"]:
            cardData[cardName]["zScoreOH"] = (float(card["OH WR"][:-1]) - OH_WRμ)/OH_WRσ
            cardData[cardName]["zScoreOH"] = float(str(cardData[cardName]["zScoreOH"])[:5])
        if card["IWD"]:
            cardData[cardName]["zScoreIWD"] = (float(card["IWD"][:-2]) - IWDμ)/IWDσ
            cardData[cardName]["zScoreIWD"] = float(str(cardData[cardName]["zScoreIWD"])[:5])

    result["cardData"] = cardData
    result["generalStats"] = {"OH WR": OH_WRStats,
                              "GIH WR": GIH_WRStats,
                              "IWD": IWDStats}

    return result

# puts data into a master json
def processDataToMaster(colorPair, data, originalMaster):
    newMaster = originalMaster

    makeNewCards = False
    if not list(newMaster.keys()):
        makeNewCards = True

    for cardName, cardData in data["cardData"].items():
        if makeNewCards:
            newMaster[cardName] = {}
        newMaster[cardName]["ALSA"] = cardData["ALSA"]
        newMaster[cardName]["name"] = cardName
        newMaster[cardName]["color"] = cardData["Color"]
        newMaster[cardName][colorPair] = {
            "GIH WR": cardData["GIH WR"],
            "zScoreGIH": cardData["zScoreGIH"],
            "OH WR": cardData["OH WR"],
            "zScoreOH": cardData["zScoreOH"],
            "IWD": cardData["IWD"],
            "zScoreIWD": cardData["zScoreIWD"],
            "# GIH": cardData["# GIH"],
            "# OH": cardData["# OH"],
            "# GNS": cardData["# GNS"],
            "# GD": cardData["# GD"]
        }

    return newMaster


# the additions list is a list of strings to add to the url. the base url
# is handled first.
additions = ["&colors=WU", "&colors=WB", "&colors=WR", "&colors=WG",
             # W color pairs
             "&colors=UB", "&colors=UR", "&colors=UG",  # U color pairs
             "&colors=BR", "&colors=BG",  # B color pairs
             "&colors=RG"  # R color pairs
             ]

import ANSI

statistics = {}
master = {}
coloredColors = {
    "WU": f"{ANSI.pureWhite}W{ANSI.reset}{ANSI.blue}U{ANSI.reset}",
    "WB": f"{ANSI.pureWhite}W{ANSI.reset}{ANSI.dimWhite}B{ANSI.reset}",
    "WR": f"{ANSI.pureWhite}W{ANSI.reset}{ANSI.red}R{ANSI.reset}",
    "WG": f"{ANSI.pureWhite}W{ANSI.reset}{ANSI.green}G{ANSI.reset}",
    "UB": f"{ANSI.blue}U{ANSI.reset}{ANSI.dimWhite}B{ANSI.reset}",
    "UR": f"{ANSI.blue}U{ANSI.reset}{ANSI.red}R{ANSI.reset}",
    "UG": f"{ANSI.blue}U{ANSI.reset}{ANSI.green}G{ANSI.reset}",
    "BR": f"{ANSI.dimWhite}B{ANSI.reset}{ANSI.red}R{ANSI.reset}",
    "BG": f"{ANSI.dimWhite}B{ANSI.reset}{ANSI.green}G{ANSI.reset}",
    "RG": f"{ANSI.red}R{ANSI.reset}{ANSI.green}G{ANSI.reset}",
}

for addition in additions:
    totalURL = baseURL + addition
    totalURLBonusSheet = baseURLBonusSheet + addition
    # print color pair:
    colorPair = addition[-2:]
    coloredColorPair = coloredColors[colorPair]
    print(f'🍉 {coloredColorPair} {totalURL}')

    with open(f"cardRatingsTop/{colorPair}.json", "w") as cardDataJSON:
        data = fetchData(totalURL)
        if bonusSheetToggle:
            data.extend(fetchData(totalURLBonusSheet))
        processedData = processData(data)
        cardDataJSON.write(json.dumps(processedData))
        statistics[colorPair] = processedData["generalStats"]
        master = processDataToMaster(colorPair, processedData, master)

print(f'🍊 {baseURL}')
with open("cardRatingsTop/all.json", "w") as cardDataJSON:
    data = fetchData(baseURL)
    if bonusSheetToggle:
        data.extend(fetchData(baseURLBonusSheet))
    processedData = processData(data)
    cardDataJSON.write(json.dumps(processedData))
    statistics["all"] = processedData["generalStats"]
    master = processDataToMaster("all", processedData, master)

with open("cardRatingsTop/master.json", "w") as masterJSON:
    json.dump(master, masterJSON)

with open("cardRatingsTop/statistics.json", "w") as statisticsJSON:
    json.dump(statistics, statisticsJSON)
