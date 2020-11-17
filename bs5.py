import requests
from bs4 import BeautifulSoup
import time


def saveImg(imgUrl, title):
    print('저장중')
    # print(imgUrl[-4:])
    # print(title)
    title = title.replace(':', "")
    title = title.replace('(', '')
    title = title.replace(')', '')
    title = title.replace('/', '')
    title = title.replace('?','')
    filename = 'img\\' + title + imgUrl[-4:]
    # print(filename)

    r = requests.get(imgUrl)

    with open(filename, 'wb') as f1:
        f1.write(r.content)

#
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
#         img = trs[i].find('td').find('img')['src']
#         # print(img)
#
#         td1 = trs[i].find('td', class_='title')
#         title = td1.find('a').text
#
#         saveImg(img, title)
#         div = trs[i].find('div', class_='rating_type')
#         rating = div.strong.text
#         # print(rating)
#         regdate = trs[i].find('td', class_='num').text
#         # print('{},{},{}'.format(title, rating, regdate))
#         f.write('{},{},{}\n'.format(title, rating, regdate))
#

# 모든 페이지의 이미지를 다운로드 하고, 제목, 평점, 등록일을 webtoon.csv 파일로 저장
# 단 한 페이지 수집 후 1초 쉬기


with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
    for page in range(1, 7):
        url = 'https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)
        recvd = requests.get(url)

        dom = BeautifulSoup(recvd.text, 'lxml')
        table = dom.find('table', class_='viewList')
        # print(table)
        trs = table.find_all('tr')
        # print(len(trs))

        for i in range(2, len(trs)):
            img = trs[i].find('td').find('img')['src']
            # print(img)

            td1 = trs[i].find('td', class_='title')
            title = td1.find('a').text

            saveImg(img, title)
            div = trs[i].find('div', class_='rating_type')
            rating = div.strong.text
            # print(rating)
            regdate = trs[i].find('td', class_='num').text
            # print('{},{},{}'.format(title, rating, regdate))
            f.write('{},{},{}\n'.format(title, rating, regdate))

        time.sleep(1)