import requests as req
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
r = req.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)

print(soup.find_all('a'))