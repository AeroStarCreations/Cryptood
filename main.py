# It all starts here

import feedparser

coin_desk_feed = feedparser.parse('https://www.coindesk.com/feed')

first_entry = coin_desk_feed.entries[0]

for key, value in first_entry.items():
    print(f'{key}:\t{value}')