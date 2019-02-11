import urllib3
from bs4 import BeautifulSoup
import re


def ddscrape():
    page = urllib3.PoolManager()
    url = 'http://digitaldripped.com/topsongs'
    response = page.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")
    soup.prettify()
    count = 0
    anchor = soup.findAll('script')
    DDTop100 = anchor[12].text
    DDTop100 = re.findall('"artist":"(.*?)","title":"(.*?)",', DDTop100)
    # song = re.findall('"(.*?)"', DDTop100)
    for anchor in DDTop100:
        song = anchor[1]
        artist = anchor[0].replace('"', '')
        artist = artist.replace(':', ' ')
        artist = artist.replace('uring', '.')
        artist = artist.replace(',', ' ')
        print(artist, song)

ddscrape()