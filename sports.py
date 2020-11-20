import requests
import json

with open('d:\\study\\pj1\\data\\sport.csv', 'a', encoding='utf-8') as f:

    url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd = requests.get(url)
    dic = json.loads(recvd.text)
    for i in dic['list']:
        str = '{}::{}\n'.format(i['title'], i['subContent'])
        f.write(str)

# pip install pyinstaller
# pyinstaller sports.py
# pyinstaller --onefile sports.py