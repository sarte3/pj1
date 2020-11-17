# www.naver.com/robots.txt
import requests
from bs5 import BeautifulSoup
import time

# url = 'https://finance.naver.com/marketindex/'
#
# recvd = requests.get(url)
# # print(recvd)
# # print(recvd.text)
#
# dom = BeautifulSoup(recvd.text, 'lxml')
# span = dom.find('span', class_='value')
# print(span.text)

# print('-'*30)
# with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
#     url = 'https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
#     recvd = requests.get(url)
#     # print(recvd)
#
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     table = dom.find('table', class_='viewList')
#     # print(table)
#     trs = table.find_all('tr')
#     # print(len(trs))
#
#     for i in range(2, len(trs)):
#         td1 = trs[i].find('td', class_='title')
#         title = td1.find('a').text
#         div = trs[i].find('div', class_='rating_type')
#         rating = div.strong.text
#         # print(rating)
#         regdate = trs[i].find('td', class_='num').text
#         print('{},{},{}'.format(title, rating, regdate))
#         f.write('{},{},{}\n'.format(title, rating, regdate))

print('-'*30)


def saveImg(imgurl):
    print('저장중')


with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
    for page in range(1, 6+1):
        pageurl = 'https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)

        recvd = requests.get(pageurl)

        dom = BeautifulSoup(recvd.text, 'lxml')
        table = dom.find('table', class_='viewList')
        trs = table.find_all('tr')

        for i in range(2, len(trs)):
            img = trs[i].find('td').find('img')['src']
            saveImg(img)
            td1 = trs[i].find('td', class_='title')
            title = td1.find('a').text
            div = trs[i].find('div', class_='rating_type')
            rating = div.strong.text
            regdate = trs[i].find('td', class_='num').text
            f.write('{},{},{},{}\n'.format(img, title, rating, regdate))

