# mariadb-10.3.27-winx64.msi
# show databases; 데이터베이스 목록 확인
# use pythondb; 사용할 데이터베이스 선택
# show tables; 선택된 데이터베이스의 테이블 목록 확인
# import pymysql as my
# 1) 데이터베이스 연결
# con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2) 커서 생성
# # cur = con.cursor()
# cur = con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# sql = 'select * from member'
# # 4) 실행 처리
# cur.execute(sql)
# rows = cur.fetchall()
# for row in rows:
#     print(row)
#     print(row['no'], row['name'], row['age'], row['email'], row['birthyear'])
# # 5) 자원 해제
# con.close()

# 1) 데이터베이스 연결
# con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2) 커서 생성
# # cur = con.cursor()
# cur = con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# while True:
#     name = input('사용자 이름=')
#     if name == '':
#         break
#     age = input('사용자 나이=')
#     email = input('사용자 이메일=')
#     birthyear = input('사용자 태어난 년도=')
#     sql = 'insert into member (name, age, email, birthyear) values(%s, %s, %s, %s)'
#     # 4) 실행 처리
#     cur.execute(sql, (name, age, email, birthyear))
# con.commit()
# # 5) 자원 해제
# con.close()

# # 1) 데이터베이스 연결
# con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# # 2) 커서 생성
# # cur = con.cursor()
# cur = con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# age = input('나이 = ')
# sql = 'delete from member where age<=%s'
# # 4) 실행 처리
# cur.execute(sql, (age,))
# # 튜플은 값이 하나라도 ,를 찍어 줘야 함
# con.commit()
# # 5) 자원 해제
# con.close()

# 이름과 태어난 년도를 입력받아 나이, 태어난 년도를 수정
# con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
# cur = con.cursor(my.cursors.DictCursor)
# name = input('이름 > ')
# birthyear = input('태어난 년도 > ')
# sql = "update member set age =%s ,birthyear=%s where name=%s"
# age = 2020-int(birthyear)+1
# cur.execute(sql, (age, birthyear, name))
# con.commit()
# con.close()

import pymysql as my
import requests
from bs4 import BeautifulSoup


con = my.connect(host='localhost', user='root', password='1234', db='pythondb', charset='utf8')
cur = con.cursor(my.cursors.DictCursor)
url = 'https://movie.naver.com/movie/running/current.nhn'
sql = "insert into movie(title, rating, reserve, playtime) values (%s, %s, %s, %s)"

recvd = requests.get(url)
dom = BeautifulSoup(recvd.text, 'lxml')
ul = dom.find('ul', class_='lst_detail_t1')
lis = ul.find_all('li')

for li in lis:
    img = li.find('img')['src']
    title = li.find('dt', class_='tit').find('a').text
    rating = li.find('span', class_='num').text
    reserve = li.find('div', class_='star_t1 b_star')

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
    cur.execute(sql, (title, rating, reserve, playtime))
con.commit()
con.close()
