import requests
from bs4 import BeautifulSoup
import time
import re

# Function to scrape tweets and count stock symbol mentions
def scrape_tweets(accounts, ticker, interval):
    ticker_pattern = re.compile(rf'\${ticker}')
    ticker_count = 0

    for account in accounts:
        url = f'https://twitter.com/{account}'
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tweets = soup.find_all('div', {'data-testid': 'tweet'})
            for tweet in tweets:
                tweet_text = tweet.get_text()
                ticker_count += len(ticker_pattern.findall(tweet_text))
        else:
            print(f"Failed to fetch tweets from {account}. Status code: {response.status_code}")

    return ticker_count

# Main function
def main():
    accounts = [
        "Mr_Derivatives",
        "warrior_0719",
        "ChartingProdigy",
        "allstarcharts",
        "yuriymatso",
        "TriggerTrades",
        "AdamMancini4",
        "CordovaTrades",
        "Barchart",
        "RoyLMattox"
    ]
    ticker = input("Enter the stock ticker (e.g., TSLA): ").strip()
    interval = int(input("Enter the time interval for scraping in minutes: ").strip())

    while True:
        ticker_count = scrape_tweets(accounts, ticker, interval)
        print(f"'{ticker}' was mentioned {ticker_count} times in the last {interval} minutes.")
        time.sleep(interval * 60)

if __name__ == "__main__":
    main()
