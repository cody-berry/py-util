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
        print("Failed to fetch data.")
        return None


# the url that handles the expansion for LTR
LTRbaseURL = (f'https://www.17lands.com/card_ratings/data?expansion=LTR'
              '&format=PremierDraft'
              '&start_date=2023-05-28'
              '&end_date=2023-07-06')
print(LTRbaseURL)

# with open("cardRatingsAuto/all.json", "w") as cardDataJSON:
#     cardDataJSON.write(str(fetchData(LTRbaseURL)))

# the additions list is a list of strings to add to the url. the base url
# is handled first.
additions = ["&colors=WU", "&colors=WB", "&colors=WR", "&colors=WG",
             # W color pairs
             "&colors=UB", "&colors=UR", "&colors=UG",  # U color pairs
             "&colors=BR", "&colors=BG",  # B color pairs
             "&colors=RG"  # R color pairs
             ]

for addition in additions:
    totalURL = LTRbaseURL + addition
    print(totalURL)
