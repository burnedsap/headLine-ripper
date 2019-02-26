import requests
from bs4 import BeautifulSoup
pages = []
b = 31
new_path = '/Users/username/Documents/folder/input.txt'
new_days = open(new_path,'w')

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
        url = 'https://www.thehindu.com/archive/print/2018/' + str(j)+ '/' + str(i) + '.htm'
        pages.append(url)

    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        artist_name_list = soup.find(class_='tpaper-container')
        artist_name_list_items = artist_name_list.find_all(class_='archive-list')


        for artist_name in artist_name_list_items:
            names = artist_name
            art_n = names.find_all('a')

            for head in art_n:
                headL = head.contents[0]
                print(headL)
                new_days.write(headL)
new_days.close()
