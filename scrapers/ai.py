from exa_py import Exa
import os
from dotenv import load_dotenv

load_dotenv()

exa = Exa(os.getenv("EXA_API_KEY"))

results = exa.search(
    "coles 3L whole milk price",
    num_results=1
)

print(results)
