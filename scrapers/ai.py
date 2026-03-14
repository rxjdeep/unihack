from exa_py import Exa
import os
from dotenv import load_dotenv

load_dotenv()

exa = Exa(os.getenv("EXA_API_KEY"))

def search_product(query):
    response = exa.search(query, num_results=1)

    products = []

    for r in response.results:
        products.append({
            "title": r.title,
            "url": r.url
        })

    return products

products = search_product("coles 3L whole milk price")

print(products)




