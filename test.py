import requests
from bs4 import BeautifulSoup

"""
name = input('ID:')
response = requests.get('https://lol.moa.tw/summoner/show/{}'.format(name))
"""
response = requests.get('https://lol.moa.tw/summoner/show/54978')
data = BeautifulSoup(response.text,'html.parser')
tag = 'div.col-xs-6 dl.dl-horizontal.sub-jumbotron.h3 dd'
rank = data.select(tag)
for i in range(3,6) :
    print('S{} :'.format(i+3),rank[i].text)