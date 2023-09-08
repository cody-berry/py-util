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

print(fetchData(f'https://www.17lands.com/card_ratings/data?expansion=LTR'
                f'&format=PremierDraft'))
