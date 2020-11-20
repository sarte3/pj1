# import os
# import sys
# import urllib.request
# import json

# with open('data\\blog.csv', 'w', encoding='utf-8') as f:
#
#     client_id = "twrhEE4LU8HoKxIrMwzM"
#     client_secret = "hsPSocfNRK"
#     encText = urllib.parse.quote("성탄절")
#
#     for i in range(1, 902, 100):
#         url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=".format(i) + encText # json 결과
#         # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#         request = urllib.request.Request(url)
#         request.add_header("X-Naver-Client-Id",client_id)
#         request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         if(rescode==200):
#             response_body = response.read()
#             result = response_body.decode('utf-8')
#         else:
#             print("Error Code:" + rescode)
#
#         dic = json.loads(result)
#         for item in dic['items']:
#             title = item['title']
#             description = item['description']
#             str = '{}::{}\n'.format(title, description)
#             # print(str)
#             f.write(str)

# print('-'* 30)
#
# import os
# import sys
# import urllib.request
# import json
#
#
# client_id = "twrhEE4LU8HoKxIrMwzM"
# client_secret = "hsPSocfNRK"
# encText = urllib.parse.quote("가을")
# url = "https://openapi.naver.com/v1/search/movie.json?start=1&display=100&query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
#
# dic = json.loads(result)
# print(dic)
# # for item in dic['items']:
# #     title = item['title']
# #     description = item['description']
# #     str = '{}::{}\n'.format(title, description)
# #     print(str)

import os
import sys
import urllib.request
import json

with open('data\\ihaveadream.txt', 'r', encoding='utf-8') as f:
    client_id = "PPGPj5Rdmo91C3C73Ycm"
    client_secret = "tTcZSB2Hhz"

    str = f.read()
    lines = str.split('\n')

    for i in lines:
        encText = urllib.parse.quote('안녕하세요')
        data = "source=en&target=ko&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            result = json.loads(result)
            dic = result['message']
            trans = dic['result']['translatedText']
            print(trans)
        else:
            print("Error Code:" + rescode)

# i have a dream 을 검색하여 한국어로 번역하세요