import requests
from bs4 import BeautifulSoup
import lxml

#url ="https://www.amazon.in/Redmi-K20-Glacier-Storage-Exchange/dp/B082FNDQT7/ref=sxin_2?asc_contentid=amzn1.osa.409753bd-53db-4cb0-bb3e-77d884a6377f.A21TJRUUN4KGV.en_IN&asc_contenttype=article&ascsubtag=amzn1.osa.409753bd-53db-4cb0-bb3e-77d884a6377f.A21TJRUUN4KGV.en_IN&creativeASIN=B082FNDQT7&cv_ct_cx=mi+phones&cv_ct_id=amzn1.osa.409753bd-53db-4cb0-bb3e-77d884a6377f.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&dchild=1&keywords=mi+phones&linkCode=oas&pd_rd_i=B082FNDQT7&pd_rd_r=7bb0da8d-ba64-42aa-a3ba-facf829e5148&pd_rd_w=Pxy6m&pd_rd_wg=AAVBG&pf_rd_p=6567d3a4-28dd-430b-a035-b0af9623dfa4&pf_rd_r=QJ2DS91MVJC7FYHE5059&qid=1620472571&sr=1-2-c84eb971-91f2-4a4d-acce-811265c24254&tag=timessyndicat-21"
#url="https://www.amazon.in/Brooks-Ghost-Primer-Pearl-Medium/dp/B0842NGF6P/ref=sr_1_1_sspa?dchild=1&keywords=shoes&qid=1620472644&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUk1USTlIWkcwQUpNJmVuY3J5cHRlZElkPUEwOTM3NDY5VlBPMklXQkVHTDZBJmVuY3J5cHRlZEFkSWQ9QTA5Njc4NDczTEdNM1hTWTZCOU84JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
#url = "https://www.amazon.in/Boat-Rockerz-450-Lightweight-Compatibility/dp/B08667772G/ref=sr_1_1_sspa?dchild=1&keywords=headphones&qid=1620472697&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWkFaN0dZSlpBMDIzJmVuY3J5cHRlZElkPUEwMTQ1NTE3M0FZREpQVUpPSkpQViZlbmNyeXB0ZWRBZElkPUEwOTI4OTU3MVBYSTFaNjhaOEpXUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
# url="https://www.amazon.in/AU-A04TR-Condenser-Cardioid-Microphone-Sampling/dp/B07WQWBJNC/ref=sr_1_2_sspa?dchild=1&keywords=mic&qid=1623181623&smid=A14CZOWI0VEHLG&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNlJEU1FSRkhOUE8mZW5jcnlwdGVkSWQ9QTA1NjA3MTYxTEZZWVVTV0ROWjZGJmVuY3J5cHRlZEFkSWQ9QTA1OTQ2ODYzUzZXWDRTVUNMMjJCJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

def get_link_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        'Accept-Language': "en",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    price= soup.select_one("#priceblock_ourprice")
    if(price==None):
        price=soup.select_one("#priceblock_dealprice")
    if(price==None):
        price=soup.select_one("#priceblock_bestprice")
    price=price.getText()

    # td = soup.find('td', {'class': 'a-span12'})
    # children = td.findChildren("span" , recursive=False)
    # price = children[0].getText()
    price = float(price[2:].replace(",",""))
    print(price)
    return name,price
