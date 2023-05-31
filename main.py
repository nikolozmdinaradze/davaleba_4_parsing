from bs4 import BeautifulSoup
import requests
from time import sleep
import csv

file = open('cpus.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['name', 'price', 'link'])



for page_num in range(1, 7):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=cpu&_sacat=0&_pgn={page_num}'
    request = requests.get(url)
    html = request.text
    sleep(15)
    soup = BeautifulSoup(html, 'html.parser')

    heads = soup.find_all('span', role='heading')
    price = soup.find_all('span', {'class':'s-item__price'})
    link = soup.find_all('a',{'class':'s-item__link'})
    i = 1 #თვლა გამიზნულად არ დავაწყებინე 0-დან, რადგან იმავე ტაგში შეუსაბამო მონაცები იყო.
    while True:
        try:
            csv_obj.writerow([heads[i].text, price[i].text, link[i]['href']])
            i+=1
        except IndexError:
            break