# 영화제목, 점수, 예매율, 상영시간을 추출하여 movie.csv 저장
# 영화 포스터는 img폴더에 저장
# from bs4 import BeautifulSoup
# import requests

# with open('data\\movie.txt', 'w', encoding='utf-8') as f:
#     recvd = requests.get('https://movie.naver.com/movie/running/current.nhn')
#
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     li = dom.find('ul', class_='lst_detail_t1').find_all('li')
#     for l in li:
#         title = l.find('dt', class_='tit').find('a').text
#         rating = l.find('div', class_='star_t1').find('span', class_='num').text+'%'
#         book = ''
#
#         if l.find('div', class_='b_star') == None :
#             book = ''
#         else:
#             book = l.find('div', class_='b_star').find('span', class_='num').text
#         runTime = l.find('dl', class_='info_txt1').find('span', class_='split').next_sibling
#         runTime = runTime.strip()
#         imgUrl = l.find('div', class_='thumb').find('img')['src']
#
#         filename = 'img\\' + title + '.jpg'
#         # print(filename)
#
#         r = requests.get(imgUrl)
#
#         with open(filename, 'wb') as f1:
#             f1.write(r.content)
#
#         f.write('{},{},{},{}\n'.format(title, rating, book, runTime))
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://movie.naver.com/movie/running/current.nhn'
# recvd = requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom = BeautifulSoup(recvd.text, 'lxml')
# ul = dom.find('ul', class_='lst_detail_t1')
# # print(ul)
# lis = ul.find_all('li')
# # print(len(lis))
#
# for li in lis:
#     img = li.find('img')['src']
#     title = li.find('dt', class_='tit').find('a').text
#     # print(title)
#     rating = li.find('span', class_='num').text
#
#     reserve = li.find('div', class_='star_t1 b_star')
#     if reserve == None:
#         reserve = ''
#     else:
#         reserve = reserve.find('span', class_='num').text
#
#
#     # print(reserve)
#     play = li.find('dl', class_='info_txt1').text
#     playlist = play.split('|')
#     for p in playlist:
#         if p.count('분') == 1:
#             if p.count('개요') == 1:
#                 p = p.replace('개요','')
#             playtime = p.strip()
#             break
#
#     str = '%s,%s,%s,%s'%(title, rating, reserve, playtime)
#     print(str)
#

# a = '777 | apple |곰 |아아아'
# print(a.split('|'))
# print(a.split('|')[1].strip())

import requests
import os
from bs4 import BeautifulSoup


def saveImg(imgUrl, title):
    # print(imgUrl)
    # print(imgUrl.index('?'))
    # print(len(imgUrl))
    # print(imgUrl[79:83])
    filename = 'img\\'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    print(filename)

    r = requests.get(imgUrl)

    with open(filename, 'wb') as f1:
        f1.write(r.content)

with open(os.path.join('data','movie.csv'), 'w', encoding='utf-8') as f:
    url = 'https://movie.naver.com/movie/running/current.nhn'
    recvd = requests.get(url)
    dom = BeautifulSoup(recvd.text, 'lxml')
    ul = dom.find('ul', class_='lst_detail_t1')
    lis = ul.find_all('li')


    for li in lis:
        img = li.find('img')['src']
        title = li.find('dt', class_='tit').find('a').text
        rating = li.find('span', class_='num').text
        reserve = li.find('div', class_='star_t1 b_star')
        saveImg(img, title)

        if reserve == None:
            reserve = ''
        else:
            reserve = reserve.find('span', class_='num').text

        play = li.find('dl', class_="info_txt1").text
        playlist = play.split('|')
        playtime = ''
        for p in playlist:
            if p.count('분') == 1:
                if p.count('개요') == 1:
                    p = p.replace('개요', '')
                playtime = p.strip()
                break
        str = '%s,%s,%s,%s\n' % (title, rating, reserve, playtime)
        f.write(str)
