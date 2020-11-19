# import requests
# from bs4 import BeautifulSoup
# import json
#
# with open('data\\sport.csv', 'w', encoding='utf-8') as f:
#
#     url = 'https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
#     recvd = requests.get(url)
#     # print(recvd)
#     # print(recvd.text)
#     dic = json.loads(recvd.text)
#     # print(dic)
#     # print(dic['list'])
#
#     for i in dic['list']:
#         str = '{}::{}\n'.format(i['title'], i['subContent'])
#         # print(str)
#         f.write(str)

# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import json
# import os
#
# # with open(os.path.join('data', 'money.csv'), 'w', encoding='utf-8') as f:
# with open(os.path.join('data', 'money.csv'), 'w') as f:
#
#     ua = UserAgent()
#     # print(ua.chrome)
#     # print(ua.ie)
#
#     headers = {'user-agent': ua.chrome, 'referer': 'https://finance.daum.net/'}
#
#
#     url = 'https://finance.daum.net/api/search/ranks?limit=10'
#     url2 = 'https://finance.daum.net/api/sectors?market=KOSPI&change=RISE&includedStockLimit=1&perPage=5'
#     url3 = 'https://finance.daum.net/api/sectors?market=KOSDAQ&change=RISE&includedStockLimit=1&perPage=5'
#
#     recvd = requests.get(url, headers=headers)
#     # print(recvd)
#     # print(recvd.text)
#
#     dic = json.loads(recvd.text)
#     for rank in dic['data']:
#         f.write('{},{},{}\n'.format(rank['rank'], rank['name'], rank['tradePrice']))
#
#     recvd =requests.get(url2, headers=headers)
#     dic = json.loads(recvd.text)
#     # print(dic)
#     for item in dic['data']:
#         print(item['sectorName'], item['includedStocks']['name'])


# 성탄절로 1000건 검색하여 제목(title)과 상세내용(description) blog.csv로 저장하세요

import os
import sys
import urllib.request
import json

with open('data\\blog.csv', 'w', encoding='utf-8') as f:

    client_id = "twrhEE4LU8HoKxIrMwzM"
    client_secret = "hsPSocfNRK"
    encText = urllib.parse.quote("성탄절")

    for i in range(1, 902, 100):
        url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=".format(i) + encText # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)

        dic = json.loads(result)
        for item in dic['items']:
            title = item['title']
            description = item['description']
            str='{}::{}\n'.format(title, description)
            print(str)
            f.write(str)
