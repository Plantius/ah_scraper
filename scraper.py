import requests 
from selenium import webdriver
from bs4 import BeautifulSoup

payload = ""
headers = {
    'authority': "www.jumbo.com",
    'cache-control': "max-age=0",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "none",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'accept-language': "en-US,en;q=0.9"
    }

def getPage(url: str):
    page = requests.request("GET", url, data=payload, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')

# url = "https://www.jumbo.com/producten/?searchType=keyword&searchTerms=brood"
# page = getPage(url).contents

# print(page[1])
url = "https://www.jumbo.com/producten/jumbo-volkoren-meergranen-brood-407055STK"
page = getPage(url).contents
print(page[1].text)
# print(getPage("https://www.ah.nl"))