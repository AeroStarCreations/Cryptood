# It all starts here

import feedparser
import time
import re
import cryptocompare
import requests
from textblob import TextBlob
from collections import defaultdict

# cryptocompare.cryptocompare._set_api_key_parameter('ea58403ce7e9d4d8f248e32ee0f39f937f96554191a83d9ab1119dc70e193a09')

start_time = time.time()
buy_count = 0
sell_count = 0

coin_desk_feed = feedparser.parse('https://www.coindesk.com/feed')
word_counts = defaultdict(lambda: 0)
desired_word_counts = defaultdict(lambda: 0)
noun_phrase_counts = defaultdict(lambda: 0)
desired_tags = ['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'RB', 'RBS', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

for entry in coin_desk_feed.entries:
    text = entry.title + entry.summary
    blob = TextBlob(text)
    buy_count += len(re.findall(r'buy\w*', text, flags=re.I))
    sell_count += len(re.findall(r'sell\w*', text, flags=re.I))
    for word in blob.word_counts:
        word_counts[word] += 1
    for noun_phrase in blob.noun_phrases:
        noun_phrase_counts[noun_phrase] += 1
    for tag in blob.tags:
        if tag[1] in desired_tags and len(tag[0]) > 2:
            desired_word_counts[tag[0].lower()] += 1
    print(f'\nTitle: {entry.title}')
    print(f'Summary: {entry.summary}')
    print(f'Sentiment: {blob.sentiment}')

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Top 10 Words')
sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]
for word_count in sorted_word_counts:
    print(f'{word_count[0]}:\t{word_count[1]}')

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Top 10 Noun Phrases')
sorted_noun_phrases_counts = sorted(noun_phrase_counts.items(), key=lambda item: item[1], reverse=True)[:10]
for noun_phrase_count in sorted_noun_phrases_counts:
    print(noun_phrase_count)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Top 10 Desired Words')
sorted_desired_word_counts = sorted(desired_word_counts.items(), key=lambda item: item[1], reverse=True)[:10]
for word_count in sorted_desired_word_counts:
    print(word_count)

# print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print('Current Prices:')
# print(f'{cryptocompare.get_price("BTC", "USD")}')
# print(f'{cryptocompare.get_price("ETH", "USD")}')

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Buy count: {buy_count}')
print(f'Sell count: {sell_count}')
print(f'\nRuntime: {time.time()-start_time} seconds')
