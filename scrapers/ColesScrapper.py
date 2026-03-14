import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.5"
}

def get_product_details(product_url: str) -> dict:
    product_details = {}

    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    title_tag = soup.find("h1", class_="product__title")
    price_tag = soup.find("div", class_="price")

    if title_tag is not None:
        tit = str(soup.title)
        title_tag["title"] = tit[20:]
    else:
        product_details["title"] = "Title not found"

    if price_tag is not None:
        product_details["price"] = price_tag.get_text(strip=True)
    else:
        product_details["price"] = "Price not found"

    looksmax(product_details)

def looksmax(details: dict) -> str:
    for key, value in details.items():
        print(value) 
    

if __name__ == "__main__":
    product_url = input("Enter product url: ")
    get_product_details(product_url)