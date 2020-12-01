import urllib.request
url='https://1.bp.blogspot.com/-tL1MsUqLebw/WdkQQiJD9II/AAAAAAAACJE/KkVZQoS5x9EXApgavJqlU7VyTO0GH_pSwCLcBGAs/s1600/d65f733e920d3d97c650b2ef2f9c1766_EROOJ3_ZQz98r_TGE.gif'
filename = 'img\\sana.gif'
urllib.request.urlretrieve(url, filename)

from urllib.parse import urlparse
url = 'https://www.ml502.co.kr:1621/a502/index.html?student=14&area=60'
pr = urlparse(url) #네임드튜플 반환
print(pr)
print(pr.scheme) #http, ftp ...
print(pr.netloc) #네트웍 위치
print(pr.path) # 경로
print(pr.query)

from urllib.parse import urljoin
baseurl='https://www.ml5.co.kr:1621/green/a502/index.html'
print(1,urljoin(baseurl,'a.html'))
print(2, urljoin(baseurl,'b.html'))
print(3, urljoin(baseurl,'/c.html'))
print(4, urljoin(baseurl,'//d.html'))
print(5, urljoin(baseurl,'blue/e.html'))
print(6, urljoin(baseurl,'/blue/e.html'))
print(7, urljoin(baseurl,'http://f.html'))
print(urljoin(baseurl,'../a501/c.html'))

import os
# name1=os.path.join('d:\\','study','pj1','data','Beauty.smi')
# name2=os.path.join('d:\\','study','pj1','data')
# print('name1',name1)
# print('name1의 dirname',os.path.dirname(name1))
# print('name1의 basename',os.path.basename(name1))
# print('-'*30)
# print('name2',name2)
# print('name2의 dirname',os.path.dirname(name2))
# print('name2의 basename',os.path.basename(name2))
# print(os.path.exists('d:\\study\\pj1\\data'))
# print(os.path.exists('d:\\study\\pj1\\data2'))
# if not os.path.exists('d:\\study\\pj1\\data2'):
#     os.mkdir('d:\\study\\pj1\\data2')
a=[i for i in range(5)]
print(a)
b=['one','two','three']
print(b)
a=a+b
print(a)
a.append(b)
print(a)