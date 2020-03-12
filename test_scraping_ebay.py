import requests
from bs4 import BeautifulSoup

#declaration requests
html_requests = requests.get('https://www.ebay.com/sch/i.html',
                             params={'_from':'R40','_trksid':'m570.l1313','_nkw':'iphone','_sacat':'0'})
#declaration BeautifulSoup
soup = BeautifulSoup(html_requests.text, 'html.parser')

#Scrapper
product_image = soup.find_all(attrs={'class': 's-item__image'})

for img in product_image:
    print(img.find('img')['alt'])
#print(product_image)