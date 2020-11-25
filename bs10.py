import requests
import re
# url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
# recvd = requests.get(url)
# # print(recvd)
# # re.DOTALL : 줄바꿈까지 포함
# locations = re.findall(r'<location wl_ver="3">(.+?)</location>', recvd.text, re.DOTALL)
# # print(len(locations))
# for location in locations:
#     # print(location)
#     # province = re.findall(r'<province>(.+?)</province>', location, re.DOTALL)
#     # print(province)
#     pc = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>', location, re.DOTALL)
#     # print(pc)
#     province = pc[0][0]
#     city = pc[0][1]
#     # print(province, city)
#     datas = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
#     # print(len(datas))
#     for data in datas:
#         # print(data)
#         temps = re.findall(
#             r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>.+?<tmn>(.+?)</tmn>.+?<tmx>(.+?)</tmx>.+?<reliability>(.*?)</reliability>.+?<rnSt>(.+?)</rnSt>',
#             data, re.DOTALL)
#         # print(temps[0])
#         mode = temps[0][0]
#         tmEf = temps[0][1]
#         wf = temps[0][2]
#         tmn = temps[0][3]
#         tmx = temps[0][4]
#         reliability = temps[0][5]
#         rnSt = temps[0][6]
#         str = '{}, {}, {}, {}, {}, {}, {}, {}, {}'
#         print(str.format(province, city, mode, tmEf, wf, tmn, tmx, reliability, rnSt))

# print(re.search('ca{2}t', 'ct'))
# print(re.search('ca{2}t', 'caat'))
# print(re.search('ca{2,}t', 'caat'))
# print(re.search('ca{2,5}t', 'caaaaat'))
# print(re.search('ca?t', 'ct'))
# print(re.search('ca?t', 'cat'))
# print(re.search('ca?t', 'caat'))

# 치환
# re.sub('바꿀 문자열', '대상문자열')
color = re.compile('(blue|green|red)')
print(color.sub('pink', 'orange book and green dress and red socks'))
