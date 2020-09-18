import concurrent.futures
MAX_THREADS = 2
#40=5.182
import requests
import time
from bs4 import BeautifulSoup
pages = []
VALID_TAGS = ['div', 'p']
b = 31
#new_path = '/Users/salil/Documents/headline/url19.txt'
#new_days = open(new_path,'w')

def calculate():
    for j in range(1, 12+1):
        if j==1:
            b = 31
        if j==2:
            b = 28
        if j==3:
            b = 31
        if j==4:
            b = 30
        if j==5:
            b = 31
        if j==6:
            b = 30
        if j==7:
            b = 31
        if j==8:
            b = 31
        if j==9:
            b = 30
        if j==10:
            b = 31
        if j==11:
            b = 30
        if j==12:
            b = 31
        for i in range(1, b+1):
            url = 'https://www.thehindu.com/archive/print/2019/' + str(j)+ '/' + str(i) + '.htm'
            pages.append(url)


def main(curls):
    t0 = time.time()
    sort_url(curls)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(curls)} stories.")
    new_days.close()
    

def sort_url(curls):
    threads = min(MAX_THREADS, len(curls))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, curls)
#    for item in curls:
#        download_url(item)
    

def download_url(curlies):
#    print(curlies)
    page = requests.get(curlies)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    for alist in soup.find_all(class_='archive-list'):
        if alist != None:    
            for a in alist.find_all('a', href=True):
                links = a['href']
                new_days.write(str(links)+'\n')
#    time.sleep(0.25)

calculate()
main(pages)
