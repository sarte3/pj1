import requests
from bs4 import BeautifulSoup
import cx_Oracle

# create table webtoon(
#     no number primary key,
#     title varchar2(200),
#     rating varchar2(20),
#     regdate varchar2(50)
# );
#
# create sequence webtoon_seq;
# insert into webtoon values(webtoon_seq.nextval, title, rating, regdate)

con = cx_Oracle.connect('happy/day@localhost:1521/xe')
cur = con.cursor()
sql = 'insert into webtoon values (webtoon_seq.nextval, :1, :2, :3)'

for page in range(1, 7):
    url = 'https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)
    recvd = requests.get(url)

    dom = BeautifulSoup(recvd.text, 'lxml')
    table = dom.find('table', class_='viewList')
    trs = table.find_all('tr')

    for i in range(2, len(trs)):
        img = trs[i].find('td').find('img')['src']
        td1 = trs[i].find('td', class_='title')
        title = td1.find('a').text
        div = trs[i].find('div', class_='rating_type')
        rating = div.strong.text
        regdate = trs[i].find('td', class_='num').text
        # sql = "insert into webtoon values(webtoon_seq.nextval, '{}', '{}', '{}')".format(title, rating, regdate)
        cur.execute(sql, (title, rating, regdate))

con.commit()
con.close()
