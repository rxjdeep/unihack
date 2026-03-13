import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent" : "Mozilla/5.0",
    "Accept-language" : "en-US, en;q=0.5"
}

url1 = "https://www.coles.com.au/product/monster-energy-ultra-can-500ml-2787147?cid=col_cpc_Generic%7CColesSupermarkets%7CPLA%7CBeverage%7CAustralia%7CBroad&s_kwcid=AL!12693!3!682651538287!!!g!412033261645!&gclsrc=aw.ds&gad_source=1&gad_campaignid=20813101625&gbraid=0AAAAADzlvJcpH1Ctr47otO8EuqiLi1UUe&gclid=CjwKCAjw687NBhB4EiwAQ645di7pQh4b7JaGe1QphiFXpFpDR3KefYPnfXHMpRggLiGvxwRC8gAezRoC-dYQAvD_BwE"
url2 = "https://www.woolworths.com.au/shop/productdetails/511504?region_id=303325&utm_source=google&utm_medium=cpc&utm_campaign=WW-0001&cq_net=g&cq_src=GOOGLE&cq_cmp=SUPC-0001_Always%20On_Shopping__Specials_Search_Conversion_8458_815925_FY26_L3_Buy_National-AU&cq_med=20590926152&cq_plac=&cq_term=PRODUCT_GROUP&ds_adt=pla&cq_plt=gp&cq_gclid=CjwKCAjw687NBhB4EiwAQ645djzU_DQKsjc0PLkTGKZdcVA2xWBu8mQx8v5glvyNnIBvJabvrlZJhBoChrQQAvD_BwE&ds_de=c&ds_pc=online&ds_cr=675246019159&ds_tid=pla-2430970910572&ds_locphys=9071417&ds_pid=511504&gclsrc=aw.ds&cmpid=smsm:ds:GOOGLE:SUPC-0001_Always%20On_Shopping__Specials_Search_Conversion_8458_815925_FY26_L3_Buy_National-AU:PRODUCT_GROUP&gad_source=1&gad_campaignid=20590926152&gbraid=0AAAAACoj6t6zXGisQ8j_BTDOQRrKnx_-S&gclid=CjwKCAjw687NBhB4EiwAQ645djzU_DQKsjc0PLkTGKZdcVA2xWBu8mQx8v5glvyNnIBvJabvrlZJhBoChrQQAvD_BwE"
url3 = "https://www.aldi.com.au/product/v-v-energy-drink-250ml-000000000000661331"
url4 = "https://www.igashop.com.au/product/monster-energy-green-energy-drink-58731"

url_list = [url1,url2,url3,url4]

for url in url_list:
    page = requests.get(url, headers=headers)
    print(page.status_code)