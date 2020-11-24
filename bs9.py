# create table music(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     song varchar2(100)
# );
# create sequence music_seq;
#
# import requests
# from bs4 import BeautifulSoup
# import cx_Oracle
#
# # S_PAGENUMBER: 2
# # S_MB_CD: W0726200
# # S_HNAB_GBN: I
# # hanmb_nm: G-DRAGON
# # sort_field: SORT_PBCTN_DAY
#
# con = cx_Oracle.connect('happy/day@localhost:1521/xe')
# cur = con.cursor()
# sql = "insert into music values(music_seq.nextval, '{}', '{}', '{}')"
# for page in range(1, 3):
#     url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
#     data = {'S_PAGENUMBER': page,
#         'S_MB_CD': 'W0726200',
#         'S_HNAB_GBN': 'I',
#         'hanmb_nm': 'G-DRAGON',
#         'sort_field': 'SORT_PBCTN_DAY'}
#     recvd = requests.post(url, data=data)
#     # print(recvd)
#     # 저작물명, 가수명, 작사를 오라클에 저장
#     # dom = BeautifulSoup(recvd.text, 'lxml')
#     # divs = dom.find_all('div', class_='board col')
#     # tbody = divs[1].find('table').find('tbody')
#     # trs = tbody.find_all('tr')
#     # for i in range(len(trs)):
#     #     tds = trs[i].find_all('td')
#     #     title = tds[0].text
#     #     singer = tds[1].text
#     #     lyc = tds[2].text
#     #     print(title, singer, lyc)
#     #     cur.execute(sql.format(title, singer, lyc))
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     tables = dom.find_all('table')
#     # print(len(tables))
#     trs = tables[1].find_all('tr')
#     # print(len(trs))
#     for i in range(1, len(trs)):
#         tds = trs[i].find_all('td')
#         title = tds[0].text
#         singer = tds[1].text
#         song = tds[2].text
#         # print(title, singer, song)
#         cur.execute(sql.format(title, singer, song))
#
# con.commit()
# con.close()
#
# import requests
# from bs4 import BeautifulSoup
#
# with open('data\\kma.csv', 'w', encoding='utf-8') as f:
#     url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
#     recvd = requests.get(url)
#     # print(recvd.text)
#     # bs4
#     # 서울, 인천 경기도 - 서울
#     dom = BeautifulSoup(recvd.text, 'lxml')
#     locations = dom.find_all('location')
#     # print(len(locations))
#
#     for location in locations:
#         province = location.find('province').text
#         city = location.find('city').text
#         # print(province, city)
#         datas = location.find_all('data')
#         for data in datas:
#             mode = data.find('mode').text
#             tmEf = data.find('tmef').text
#             wf = data.find('wf').text
#             tmn = data.find('tmn').text
#             tmx = data.find('tmx').text
#             reliability = data.find('reliability').text
#             rnSt = data.find('rnst').text
#             str = '{},{},{},{},{},{},{},{},{}\n'.format(province, city, mode, tmEf, wf, tmn, tmx, reliability, rnSt)
#             # print(str)
#             # f.write(str)
# # 정규표현식식
# # 정규표현식 패키지
# import re
# str = '''3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534'''
# re.findall(r'패턴', 문자열)
# r1 = re.findall('[0-9]', str)
# print(r1)
# r1 = re.findall(r'[0-9]+', str)
# print(r1)
# r1 = re.findall(r'[A-Z]+', str)
# print(r1)
# r1 = re.findall(r'[a-z]+', str)
# print(r1)

# *(0번 이상), +(1번 이상), .(줄바꿈을 제외한 한글자), ?(0 또는 1), |(선택)
# [] 범위에 들어가는 것
# {1, 3}  (1번 이상 최대 3번까지), {, 3} (3번 이하) {1, } (1번 이상), {3} 3번
# 옵션
# re.I or re.IGNORECASE() : 대소문자 구분 x
# re.DOTALL(S) : 줄바꿈 포함
# re.VERBOSE(X) : 정규식에 주석을 사용할 수 있다
# print(re.match('a.b', 'aabrrr'))
# print(re.match('a.b', 'a0brrr'))
# print(re.match('a.b', 'c0brrr'))
# print(re.findall('a.b', 'a0brrr'))
# print(re.search('a.b', 'aabrrr'))
# str = '3pink dress'
# # match 문자열 처음부터 정규식과 일치 여부 1개만
# print(re.match('[a-z]+', str))
# # search 문자열 전체를 검색하여 일치 여부 1개만
# print(re.search('[a-z]+', str))
# # 정규식에 일치하는 문자열 반환
# print(re.findall('[a-z]+', str))
# # match 문자열 처음부터 정규식과 일치 여부
# # print(re.match('[a-z]+', str).group())
# # .group() 정규식에 일치하는 문자열 추출
# print(re.search('[a-z]+', str).group())
# str = 'pink333 dress4444'
# print(re.match('[a-z]+', str).group())
# print(re.search('[a-z]+', str).group())
# print(re.findall('[a-z]+', str))
# str = 'My handphone number 010-3333-7990'
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d', str))
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d', str).group())
# # print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d', str).group())
# print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d', str))
# print(re.findall('\d{3}-\d{4}-\d{4}', str))
# print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}', str).group())
# import re

# str = '''3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534'''
#
# # print(re.findall('[a-z]+', str, re.I))
# # t1 = re.compile('[a-z]+', re.I)
# # print(t1.findall(str))
#
# # 클립보드 조절하는 모듈 pyperclip
# import pyperclip
#
# # pyperclip.copy('hello python programming!')
# email_regex = re.compile(r'''(
#     [a-zA-Z0-9_.-]+ #username
#     @               #@ 기호
#     [a-zA-Z0-9.-]+   #도메인
#     (\.[a-zA-Z]{2,4}){1,2} #dot
#     )''', re.VERBOSE)
# text = pyperclip.paste()
# # print(text)
# result = email_regex.findall(text)
# # print(result)
# for r in result:
#     print(r[0])
import re

f = open('data\\test.html', encoding='utf-8')
text = f.read()
# print(text)
# . 줄바꿈을 제외한 한 글자
# tag = re.compile('<.+>') # 탐욕적 방식
tag = re.compile('<.+?>') # 게으른 방식
# print(tag.match(text))
# print(tag.search(text))
print(tag.findall(text))
print('-'*30)
tag = re.compile('<(.+?)>')
print(tag.findall(text))
print('-'*30)
# i로 시작하고 n으로 끝나는 모든 문자
str = 'internationalization'
test = re.compile(r'i.+n')
print(test.findall(str)) # 탐욕적 방식
# 개별로 찾고 싶을 땐 뒤에 ? 붙이기
# https://medium.com/@originerd/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-%EC%A2%80-%EB%8D%94-%EA%B9%8A%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-5bd16027e1e0
test = re.compile(r'i.+?n')
print(test.findall(str)) # 게으른 방식

# 치환
