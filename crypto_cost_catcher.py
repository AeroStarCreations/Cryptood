from bs4 import BeautifulSoup
import requests
import json
import coin_db_manager as coin_manager
import coin_cost_db_manager as coin_cost_manager
from coin import Coin
from coin_cost import CoinCost
from datetime import datetime

print("This is the start of something great! lol")

COIN_MARKET_CAP_URL = 'https://coinmarketcap.com/'
NUM_OF_LISTINGS = 15

def get_top_listings():
    # Get full HTML page
    cmc_response = requests.get(COIN_MARKET_CAP_URL)
    # Create Soup object from HTML page
    cmc_soup = BeautifulSoup(cmc_response.content, 'html.parser')
    # Find the HTML object that contains the JSON data we want
    data_tag = cmc_soup.find('script', id='__NEXT_DATA__') # type: bs4.element.Tag
    # Create the JSON object
    cmc_json = json.loads(data_tag.contents[0])
    # Retrieve all listings
    listings = cmc_json['props']['initialState']['cryptocurrency']['listingLatest']['data']
    # Sort the listings by rank
    listings.sort(key=lambda entry: entry['rank'])
    # Return the top NUM_OF_LISTINGS
    return listings[:NUM_OF_LISTINGS]

## Get top 15 currencies
listings = get_top_listings()
for i in range(15):
    print(f'{listings[i]["name"]} ({listings[i]["symbol"]}): ${listings[i]["quote"]["USD"]["price"]:,.3f}')
    # Update the coin registry
    coin_manager.insert_coin(Coin(
        listings[i]["symbol"],
        listings[i]["name"],
        listings[i]["slug"],
        listings[i]["max_supply"]
    ))
    # Save the coin cost
    coin_cost_manager.insert_coin_cost(CoinCost(
        listings[i]['symbol'],
        listings[i]['quote']['USD']['price'],
        listings[i]['last_updated'],
        listings[i]['quote']['USD']['percent_change_1h'],
        listings[i]['quote']['USD']['percent_change_24h'],
        listings[i]['quote']['USD']['percent_change_7d'],
        listings[i]['quote']['USD']['percent_change_30d'],
    ))

# Example JSON entry:
#
# {
#   "id": 1,
#   "name": "Bitcoin",
#   "symbol": "BTC",
#   "slug": "bitcoin",
#   "max_supply": 21000000,
#   "circulating_supply": 18627943,
#   "total_supply": 18627943,
#   "last_updated": "2021-02-13T22:17:02.000Z",
#   "quote": {
#     "USD": {
#       "price": 47151.56392381112,
#       "volume_24h": 69721195906.17899,
#       "percent_change_1h": 0.87666413,
#       "percent_change_24h": -1.03304962,
#       "percent_change_7d": 17.52496724,
#       "percent_change_30d": 20.74467597,
#       "market_cap": 878336645133.6099,
#       "last_updated": "2021-02-13T22:17:02.000Z"
#     }
#   },
#   "rank": 1,
#   "noLazyLoad": true
# }