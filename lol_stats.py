import requests
from bs4 import BeautifulSoup

def get_webdata(url,tag):
    response = requests.get(url)
    data = BeautifulSoup(response.text,'html.parser')
    web_data = data.select(tag)    
    return web_data

def get_ajax_url(url,tag):
    stats = get_webdata(url,tag)
    for stat in stats:   
        if stat['data-url'].find('/Ajax/aggregate/') == 0:
            ajax_url = stat['data-url']        
            break
    ajax_url = ajax_url[:-1]
    return ajax_url

def main():    
    profile_tag = 'div.col-xs-6 dl.dl-horizontal.sub-jumbotron.h3'   
    stats_tag = 'ul.nav.nav-tabs li.dropdown ul.dropdown-menu li a'    
    kda_tag = 'tr th h3'
    record_tag = 'tbody tr td'
    var = 1
    while var == 1:
        name = input('ID:')
        if name == 'exit':
            break        
        profile_url = 'https://lol.moa.tw/summoner/show/'+name
        stats_url = 'https://lol.moa.tw' + get_ajax_url(profile_url, stats_tag)
        rank = get_webdata(profile_url,profile_tag)
        rank = rank[0].text.split()
        season = 3
        for i in range(0,len(rank),2):
            if rank[i+1] != '未參與積分':        
                kda = get_webdata(stats_url + str(season),kda_tag)
                record = get_webdata(stats_url + str(season),record_tag)                            
                record = record[0].text.split()
                kda = kda[0].text.split()
                print(rank[i], rank[i+1], kda[1], kda[2], record[0],
                    record[1], record[2], record[3], record[4], record[5])
                season = season + 1
            else:
                print(rank[i], rank[i+1])
                season = season + 1

if __name__ == '__main__' :
    main()
