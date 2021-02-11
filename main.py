# It all starts here

import feedparser
import time
import re
from textblob import TextBlob

start_time = time.time()
buy_count = 0
sell_count = 0

# Random comment (delete at will)

coin_desk_feed = feedparser.parse('https://www.coindesk.com/feed')

for entry in coin_desk_feed.entries:
    text = entry.title + entry.summary
    blob = TextBlob(text)
    buy_count += len(re.findall(r'buy\w*', text, flags=re.I))
    sell_count += len(re.findall(r'sell\w*', text, flags=re.I))
    print(f'Title: {entry.title}')
    print(f'Summary: {entry.summary}')
    print(f'Sentiment: {blob.sentiment}\n')

print(f'\nBuy count: {buy_count}')
print(f'Sell count: {sell_count}')
print(f'\nRuntime: {time.time()-start_time} seconds')

# first_entry = coin_desk_feed.entries[0]

# print(f'len: {len(coin_desk_feed.entries)}')

# for key, value in first_entry.items():
#     print(f'{key}:\t{value}')