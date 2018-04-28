import requests
from bs4 import BeautifulSoup

"""
name = input('ID:')
url = 'https://lol.moa.tw/summoner/show/'+name
response = requests.get(url)
"""
url = 'https://lol.moa.tw/summoner/show/54978'
response = requests.get(url)
data = BeautifulSoup(response.text,'html.parser')
porfile_tag = 'div.col-xs-6 dl.dl-horizontal.sub-jumbotron.h3'   
stats_tag = 'ul.nav.nav-tabs li.dropdown ul.dropdown-menu li a'  

stats = data.select(stats_tag)
for stat in stats:   
    if stat['data-url'].find('/Ajax/aggregate/') == 0:
        ajax_url = stat['data-url']        
        break

ajax_url = ajax_url[:-1]

stats_url = 'https://lol.moa.tw' + ajax_url

rank = data.select(porfile_tag)
rank = rank[0].text.split()
for i in range(0,len(rank),2) :
    print(rank[i],rank[i+1])
       
response = requests.get(stats_url+'3')
data = BeautifulSoup(response.text,'html.parser')
tag = 'div.label.label-danger'
kda = data.select(tag)
print(kda[0].text)