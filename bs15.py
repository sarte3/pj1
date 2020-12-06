# 네이버 api 이용하여 '머신 러닝' 책을 검색하여
# 책제목, 책 이미지, 저자, 가격, 출판사, 상세설명 200건 데이터베이스에 저장
# 데이터베이스 종류는 자유 선택
# select count(*) from book;
# select * from book;
# desc book;
# 의 결과를 화면 캡처로
# 1) 9시 전에 반드시 큐알체크
# 2) 1교시 내에 신호전송을 하면 큐알
# 3) 매 수업 시작시 얼굴이 보이는 상태 화면 캡처
# 매 수업의 종료시 얼굴이 보이는 상태 화면 캡처
# 4) 5시 40분 이후 큐알
# 5) 5시 40~5시 50분 전에 신호전송 하면 큐알
# 화면 캡처 16번 큐알 4번이 되어야 출석 처리

import os
import sys
import urllib.request
import json
import cx_Oracle

con = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = con.cursor()
sql = "insert into book values(book_seq.nextval,'{}','{}','{}','{}','{}','{}')"

client_id = "twrhEE4LU8HoKxIrMwzM"
client_secret = "hsPSocfNRK"
encText = urllib.parse.quote("머신 러닝")
for i in range(1, 101+1, 100):
    url = "https://openapi.naver.com/v1/search/book?start={}&display=100&query=" + encText # json 결과
    request = urllib.request.Request(url.format(i))
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        infos = json.loads(response_body.decode('utf-8'))
        # print(infos)
        items = infos['items']
        for item in items:
            title = item['title']
            img = item['image']
            author = item['author']
            price = item['price']
            publisher = item['publisher']
            description = item['description']
            title = title.replace("'", "")
            description = description.replace("'", "")
            description = description.replace("‘", "")
            print(description)
            cur.execute(sql.format(title, img, author, price, publisher, description))
    else:
        print("Error Code:" + rescode)

con.commit()
con.close()