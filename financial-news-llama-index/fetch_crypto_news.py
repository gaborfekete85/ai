# content.py
import os, config
import beauty
import requests
from datetime import datetime, timedelta
import random
import string

# crypto_news_token = config.CRYPTO_NEWS_TOKEN
crypto_news_token = os.environ['CRYPTO_NEWS_TOKEN']

this_day_only = True
lastCount = 10
current_page=0
date_format = "%a, %d %b %Y %H:%M:%S %z"
today = datetime.now()
# today = today - timedelta(days=1)

def random_string(length=10):
    characters = string.ascii_letters + string.digits  # includes letters (both cases) and digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def leadingZero(source): 
    if source < 10: 
        return f"0{source}"
    else:
        return source

while current_page < 1001:
    current_page+=1
    url=f"https://cryptonews-api.com/api/v1/category?section=alltickers&items=10&page={current_page}&token={crypto_news_token}"
    print(f"Fetch New page: {current_page}")
    response = requests.get(url)
    if response.json()['total_pages'] is not None:
        json_data = response.json()
        # print(json_data)
        data = json_data['data']
        if len(data) == 0: 
            break
        else: 
            parsed_date = datetime.strptime(data[0]['date'], date_format)
            if this_day_only and parsed_date.date() != today.date(): 
                print(f"The date is not today: {parsed_date}")
                break

        for i in range(len(data)):
            parsed_date = datetime.strptime(data[i]['date'], date_format)
            print("News URL:", data[i]['news_url'])
            content = beauty.getContent(data[i]['news_url'])
            if not content: 
                continue

            current_file = f"{parsed_date.year}_{leadingZero(parsed_date.month)}_{leadingZero(parsed_date.day)}_{beauty.extractDomain(data[i]['news_url'])}_{random_string(length=15)}.html"
            print(f"File Name: {current_file}")
            article_filename = f"crypto_news/{current_file}"

            with open(article_filename, 'w') as f:
                f.write(content)

# for i in range(total_pages + 1):
    # print(i)

# print(beauty.getContent("https://www.forbes.com/sites/digital-assets/2024/01/12/100-billion-bitcoin-and-crypto-etf-price-crash-suddenly-accelerates-after-serious-fed-warning-hitting-ethereum-xrp-and-solana/"))