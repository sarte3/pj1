# import requests
# from bs4 import BeautifulSoup
# url='https://movie.naver.com/movie/running/current.nhn'
# recvd=requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml')
# ul=dom.find('ul',class_="lst_detail_t1")
# # print(ul)
# lis=ul.find_all('li')  #[li,li,li,....]
# # print(len(lis))
# for li in lis:
#     img=li.find('img')['src']
#     # print(img)
#     title=li.find('dt',class_ ="tit").find('a').text
#     # print(title)
#     rating=li.find('span',class_="num").text
#     # print(rating)
#     # reserv=li.find('div', class_="star_t1 b_star").find('span',class_="num").text
#     reserv=li.find('div', class_="star_t1 b_star")
#     if reserv==None :
#         temp = ''
#     else:
#         temp=reserv.find('span',class_="num").text
#     reserv=temp
#     # --------------------------------------
#     play=li.find('dl',class_ ="info_txt1").text
#     # print('**'+play+'**')
#     # print(play.split('|')[1].strip())
#     playlist=play.split('|')    #[]
#     playtime=''
#     for p in playlist:
#         if p.count('분')==1:
#             if p.count('개요')==1:
#                 p=p.replace('개요','')
#             playtime=p.strip()
#             break
#     str='%s,%s,%s,%s'%(title,rating,temp,playtime)
#     print(str)
# -------------------------------------
import requests
from bs4 import BeautifulSoup
import os
def saveImg(imgUrl,title):
    # print(imgUrl)
    # print(len(imgUrl))
    # print(imgUrl.index('?'))
    # print(imgUrl[:83])
    # print(imgUrl[79:83])
    # print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')])
    title=title.replace(':','')
    filename='img\\'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    print(filename)
    r=requests.get(imgUrl)
    with open(filename,'wb') as f1:
        f1.write( r.content)
with open(os.path.join('data','movies.csv'),'w',encoding='utf-8') as f:
    url='https://movie.naver.com/movie/running/current.nhn'
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    ul=dom.find('ul',class_="lst_detail_t1")
    lis=ul.find_all('li')
    for li in lis:
        img=li.find('img')['src']
        title=li.find('dt',class_ ="tit").find('a').text
        saveImg(img,title)
        # break
        rating=li.find('span',class_="num").text
        reserv=li.find('div', class_="star_t1 b_star")
        if reserv==None :
            temp = ''
        else:
            temp=reserv.find('span',class_="num").text
        reserv=temp
        play=li.find('dl',class_ ="info_txt1").text
        playlist=play.split('|')    #[]
        playtime=''
        for p in playlist:
            if p.count('분')==1:
                if p.count('개요')==1:
                    p=p.replace('개요','')
                playtime=p.strip()
                break
        str='%s,%s,%s,%s\n'%(title,rating,temp,playtime)
        f.write(str)
# json 문서
# xml 문서
# --------------------
# a=' 777 |    apple     |곰분    |아아아아'
# # print(a.split('|'))    #[]
# # print(   a.split('|')[1]   )
# # print(   a.split('|')[1].strip()   )
# for s in a.split('|'):
#     print(s,s.count('분'))






