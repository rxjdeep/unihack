import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.5"
}

url = "https://www.coles.com.au/product/coles-full-cream-milk-3l-8150288"

page = requests.get(url, headers=headers)
print("STATUS:", page.status_code)
print(page.text[:1500])

soup = BeautifulSoup(page.content, "lxml")
print("TITLE TAG:", soup.title)