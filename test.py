import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

soup = bs(requests.get('https://skyscraperpage.com/diagrams/').text, 'html.parser')
pprint()
