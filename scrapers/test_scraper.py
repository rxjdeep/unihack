import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0",
    "Accept-language" : "en-US, en;q=0.5"
}

url = "https://www.coles.com.au/product/monster-energy-ultra-can-500ml-2787147?cid=col_cpc_Generic%7CColesSupermarkets%7CPLA%7CBeverage%7CAustralia%7CBroad&s_kwcid=AL!12693!3!682651538287!!!g!412033261645!&gclsrc=aw.ds&gad_source=1&gad_campaignid=20813101625&gbraid=0AAAAADzlvJcpH1Ctr47otO8EuqiLi1UUe&gclid=CjwKCAjw687NBhB4EiwAQ645di7pQh4b7JaGe1QphiFXpFpDR3KefYPnfXHMpRggLiGvxwRC8gAezRoC-dYQAvD_BwE"

page = requests.get(url, headers=headers)

print(page.status_code)