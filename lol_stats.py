import requests
from bs4 import BeautifulSoup


name = input('ID:')
url = 'https://lol.moa.tw/summoner/show/'+name
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
season = 3
for i in range(0,len(rank),2) :
    response = requests.get(stats_url+str(season)) 
    season = season + 1
    data = BeautifulSoup(response.text,'html.parser')
    kda_tag = 'tr th h3'
    record_tag = 'tbody tr td'
    kda = data.select(kda_tag)
    record = data.select(record_tag)
    record = record[0].text.split()
    kda = kda[0].text.split()    
    print(rank[i], rank[i+1], kda[1], kda[2], record[0], record[1], record[2], record[3], record[4], record[5])