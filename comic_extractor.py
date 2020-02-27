import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# the webcomic site to extract images from
url = 'https://heartofgoldcomic.com/#!page-1'

# check if access to given url is possible
response = requests.get(url)
if str(response) == '<Response [200]>':
    print('Successful access to website url with ' + str(response))

soup = BeautifulSoup(response.text, "html.parser")
# soup.findAll('a')
