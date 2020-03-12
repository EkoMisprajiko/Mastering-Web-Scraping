import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

#scraping code will start here
@app.route('/')
def home():
    # declaration requests
    html_requests = requests.get('https://www.ebay.com/sch/i.html',
                                 params={'_from': 'R40', '_trksid': 'm570.l1313', '_nkw': 'iphone', '_sacat': '0'})
    # declaration BeautifulSoup
    soup = BeautifulSoup(html_requests.text, 'html.parser')
    # Scrapper
    product_image = soup.find_all(attrs={'class': 's-item__image'})

    return render_template('index.html',images=product_image)

if __name__ == '__main__':
    app.run(debug=True)