import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import datetime
import cx_Oracle

# url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
# recvd = requests.get(url)
# # print(recvd)
#
# # 상세 페이지의 차이름, 가격, 기본 정보를 데이터베이스에 입력, 목록 페이지의 이미지 car 폴더에 저장
# dom = BeautifulSoup(recvd.text, 'lxml')
# alist = dom.select('#listCont div.mode-cell.title > p > a')
# # print(len(alist))
#
# baseurl = 'https://www.bobaedream.co.kr'
# urllist = []
#
# for a in alist:
#     # print(baseurl+a['href'])
#     urllist.append(urljoin(baseurl, a['href']))
# # print(urllist)
# for detailurl in urllist:
#     r = requests.get(detailurl)
#     # print(r)
#     detaildom = BeautifulSoup(r.text, 'lxml')
#     title = detaildom.select_one('#bobaeConent div.title-area > h3').text
#     # print(title)
#     price = detaildom.select_one('#bobaeConent div.price-area > span > b').text
#     # print(price)
#     imgs = detaildom.select('#bx-pager img')
#     # print(imgs)
#     imglist = []
#     for img in imgs:
#         # print('https:'+img['src'])
#         if img['src'][2:6] == 'file':
#             imglist.append('https:'+img['src'])
#     # print(imglist)
#     infos = detaildom.select('#bobaeConent div.info-basic > div > table tr')
#     # print(len(infos))
#     # year = infos[0].select('td')[0].text
#     infolist = infos[0].text.strip().split('\n')
#     # print(infolist)
#     year = infolist[1]
#     baegi = infolist[-1]
#     infolist = infos[1].text.strip().split('\n')
#     distance = infolist[1]
#     color = infolist[-1]
#     infolist = infos[2].text.strip().split('\n')
#     trans = infolist[1]
#     guarantee = infolist[-1]
#     infolist = infos[3].text.strip().split('\n')
#     fuel = infolist[1]
#     confirm = infolist[-1]
#     if confirm == '확인사항':
#         confirm = ''
#     # print(infolist)
#     str = '{},{},{},{},{},{},{},{},{},{}'.format(title, price, year, baegi, distance, color, trans, guarantee, fuel, confirm)
#     print(str)

# pyinstaller --onefile bs14.py
# 명령프롬프트에서 실행시 윈도우 r + cmd
# d:
# cd D:\study\pj1\dist
# bs14


def saveImg(imglist, title):
    i = 0
    for imgurl in imglist:
        i = i + 1
        now = datetime.datetime.now()
        now = now.strftime('%y%m%d %H%M%S')
        # filename = os.path.join('car', title.strip()+str(i)+imgurl[-4:])
        filename = os.path.join('D:\\', 'study', 'pj1', 'car', title.strip()+'_'+now+'_'+str(i)+imgurl[-4:])
        # print(filename)
        r1 = requests.get(imgurl)
        with open(filename, 'wb') as f:
            f.write(r1.content)
    time.sleep(1)


con = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = con.cursor()
sql = "insert into car values(car_seq.nextval,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"


for page in range(1, 2):
    url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&order=S11&view_size=20'
    recvd = requests.get(url.format(page))

    # 상세 페이지의 차이름, 가격, 기본 정보를 데이터베이스에 입력, 목록 페이지의 이미지 car 폴더에 저장
    dom = BeautifulSoup(recvd.text, 'lxml')
    alist = dom.select('#listCont div.mode-cell.title > p > a')

    baseurl = 'https://www.bobaedream.co.kr'
    urllist = []

    for a in alist:
        urllist.append(urljoin(baseurl, a['href']))

    for detailurl in urllist:
        r = requests.get(detailurl)
        detaildom = BeautifulSoup(r.text, 'lxml')
        title = detaildom.select_one('#bobaeConent div.title-area > h3').text
        price = detaildom.select_one('#bobaeConent div.price-area > span > b').text
        imgs = detaildom.select('#bx-pager img')
        imglist = []

        for img in imgs:
            if img['src'][2:6] == 'file':
                imglist.append('https:'+img['src'])

        saveImg(imglist, title)

        infos = detaildom.select('#bobaeConent div.info-basic > div > table tr')
        infolist = infos[0].text.strip().split('\n')
        year = infolist[1]
        baegi = infolist[-1]
        infolist = infos[1].text.strip().split('\n')
        distance = infolist[1]
        color = infolist[-1]
        infolist = infos[2].text.strip().split('\n')
        trans = infolist[1]
        guarantee = infolist[-1]
        infolist = infos[3].text.strip().split('\n')
        fuel = infolist[1]
        confirm = infolist[-1]

        if confirm == '확인사항':
            confirm = ''

        cur.execute(sql.format(title, price, year, baegi, distance, color, trans, guarantee, fuel, confirm))
    time.sleep(1)
con.commit()
con.close()

# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     baegi varchar2(200),
#     distance varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     guarantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );

# create sequence car_seq;

# import datetime
# now = datetime.datetime.now()
# print(type(now), now)
# now = now.strftime('%y%m%d %H%M%S')
