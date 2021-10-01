import sqlite3
import requests
from bs4 import BeautifulSoup as bs


class Offer:
    def __init__(self, link, price, name):
        self.link = link
        self.price = price
        self.name = name

    def __str__(self):
        return f"{self.link} {self.price} {self.name}"


# con = sqlite3.connect('parts.db')
URL = "https://www.olx.bg/ads/q-ps4"

page = requests.get(URL)
soup = bs(page.content, "html.parser")
results = soup.find('table', id='offers_table')
offers = results.find_all(class_='offer-wrapper')

Offers = []
for offer in offers:
    try:
        price = offer.find('p', class_='price').text
        price = str(price).replace('\n', '').replace(' лв.', '')
        link = offer.find(
            'a', class_='marginright5 link linkWithHash detailsLink')['href']
        offerName = offer.find(
            'a', class_='marginright5 link linkWithHash detailsLink').text
        offerName = str(offerName).replace('\n', '')
        img = offer.find('img')
        data = {'link': link, 'offerName': offerName,
                'price': price, 'img': img['src']}
        url = 'http://127.0.0.1:3000/sendPost'
        r = requests.post(url, data)
    except:
        # print(Offer(link,price,offerName))
        print('Error')
    # print(Offer(link, price, name))
