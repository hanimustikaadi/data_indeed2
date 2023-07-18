import requests
from bs4 import BeautifulSoup

url = 'https://open.spotify.com/'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())

