#scrpr by kickflipJu

import urllib3
from bs4 import BeautifulSoup
import re
import csv
import dd

import data

#scrapes the Top 100 Hiphop songs according to HotNewHipHop.com

#last updated 07/7/2018

page = urllib3.PoolManager()
url = 'http://www.hotnewhiphop.com/top100/'
response = page.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")
soup.prettify()
file = 'hits.txt'
csvObj = open(file, 'w')
writer = csv.writer(csvObj, lineterminator='\n')
for anchor in soup.findAll(True,{'class': re.compile('chartItem-div')}):
    artist = anchor.contents[2].contents[0].contents[1].text.strip()
    song = anchor.contents[2].contents[0].contents[0].text.strip()
    rank = anchor.contents[0].contents[0].contents[0].contents[0].strip()
    hnhhviews = anchor.contents[3].contents[0].text.strip()
    hnhhlikes = anchor.contents[3].contents[1].text.strip()
    hnhhrating = anchor.contents[3].contents[2].text.strip()
    csvObj.write(song+', '+artist)
    csvObj.write('\n')

csvObj.write('\n')
csvObj.write('http://digitaldripped.com/topsongs')
csvObj.write('\n')
csvObj.write('\n')
page = urllib3.PoolManager()
url = 'http://digitaldripped.com/topsongs'
response = page.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")
soup.prettify()
count = 0
anchor = soup.findAll('script')
DDTop100 = anchor[12].text
DDTop100 = re.findall('"artist":"(.*?)","title":"(.*?)",', DDTop100)
song = re.findall('"(.*?)"', DDTop100)
for anchor in DDTop100:
    song = anchor[1]
    artist = anchor[0].replace('"', '')
    artist = artist.replace(':', ' ')
    artist = artist.replace('uring', '.')
    artist = artist.replace(',', ' ')
    print(artist, song)
    csvObj.write(song + ', ' + artist)
    csvObj.write('\n')
csvObj.close()


csvObj.close()



