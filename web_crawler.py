import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 2
    while page <= max_pages:
        url = "https://www.amazon.in/s?rh=n%3A976389031%2Cn%3A%21976390031%2Cn%3A15417300031%2Cn%3A4149418031%2Cn%3A4149470031&page=2&qid=1596569206&ref=lp_4149470031_pg_2"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("span", {'class': "a-size-medium a-color-base a-text-normal"}):
            span = link.get("span")
            print(link.string+ "\n")
            
            
trade_spider(2)
