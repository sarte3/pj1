# sqlite-tools-win32-x86-3330000.zip
# 압축해제하여 D:\sqlite에 둔다
# window + R > cmd > d: > cd D:\sqllite - sqlite3
# 프롬프트 모양이 eqlite> 로 변경됨
# .open 데이터베이스이름, 사용할 데이터베이스 저장
# .open pythondb
# .table : 현재 데이터베이스 테이블 목록
# create table member(
#     id char(4),
#     name char(20),
#     age int,
#     email char(30),
#     birthyear int
# );
# .schema 테이블명 : 테이블의 구조 확인, desc 테이블명
# insert into member values ('aaa', 'kim', 20, 'aaa@naver.com', 2001);
# insert into member values ('bbb', 'lee', 25, 'bbb@naver.com', 2003);
# select * from member;
# .header on : select 사용시 헤더 출력
# select * from member;
# .mode column : select 사용시 컬럼 모드로 출력(줄 맞춤)
# .quit
# sqlite3
# .open pythondb
# .table
# import sqlite3
# # 1) 데이터베이스 연결
# con = sqlite3.connect('d:\\sqlite\\pythondb')
# # 2) 커서 생성
# cur = con.cursor()
# # 3) 쿼리 생성
# sql = 'select * from member'
# # 4) 실행 처리
# cur.execute(sql)
# while True:
#     row = cur.fetchone()
#     if row == None:
#         break
#     # print(row)
#     print(row[0], row[1], row[2], row[3], row[4])
# # 5) 자원 해제
# cur.close()
# print('-'*30)
#
# import sqlite3
#
# # 1) 데이터베이스 연결
# con = sqlite3.connect('d:\\sqlite\\pythondb')
# # 2) 커서 생성
# cur = con.cursor()
#
# while True:
#     id = input('사용자 id=')
#     if id == '':
#         break
#     name = input('사용자 이름=')
#     age = input('사용자 나이=')
#     email = input('사용자 이메일=')
#     birthyear = input('사용자 태어난 년도=')
#
#     # 3) 쿼리 생성
#     # sql = "insert into member values('{}','{}',{},'{}',{})".format(id, name, age, email, birthyear)
#     sql = "insert into member values('"+id+"','"+name+"',"+age+",'"+email+"',"+birthyear+")"
#     print(sql)
#     # 4) 실행 처리
#     cur.execute(sql)
# con.commit()
# # 5) 자원 해제
# cur.close()

import sqlite3
# 1) 데이터베이스 연결
con = sqlite3.connect('d:\\sqlite\\pythondb')
# 2) 커서 생성
cur = con.cursor()
sql = "delete from member"
# print(sql)
# 4) 실행 처리
cur.execute(sql)
con.commit()
# 5) 자원 해제
cur.close()