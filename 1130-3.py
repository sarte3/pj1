# from urllib.parse import *
# from bs4 import BeautifulSoup
# from urllib.request import urlretrieve
# import os
# import re
# import time
# url='https://docs.python.org/3.8/library/'
# o=urlparse(url)
# # print('urlparse',o)
# savepath='./'+o.netloc+o.path
# # print('savepath=',savepath)
# # 디렉토리 유무확인
# # if savepath[-1]=='/':
# #     print('디렉토리')
# if re.search(r'/$',savepath):
#     # print('디렉토리')
#     savepath=savepath+'index.html'
# # print(savepath)
# if not os.path.exists(os.path.dirname(savepath)):
#     # os.mkdir('./docs.python.org')
#     # os.mkdir('./docs.python.org/3.8')
#     # os.mkdir('./docs.python.org/3.8/library/')
#     os.makedirs(os.path.dirname(savepath))
# urlretrieve(url,savepath)
# time.sleep(1)
# html=open(savepath,encoding='utf-8').read()
# # print(html)
# # 링크
# dom=BeautifulSoup(html,'lxml')
# link=dom.select('a')
# for a in link:
#     pageurl=urljoin(url,a['href'])
#     print(a['href'],'==>',pageurl)
#   ------------------------
from urllib.parse import *
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import re
import time
def enum_link(html,base):
    dom=BeautifulSoup(html,'lxml')
    links=dom.select('a')
    result=[]
    for a in links:
        url=urljoin(base,a['href'])
        print(a['href'],'==>',url)
        result.append(url)
    return result

def download_file(url):
    o=urlparse(url)
    savepath='./'+o.netloc+o.path
    if re.search(r"/$",savepath):
        savepath=savepath+'index.html'
    # print('savepath=',savepath)
    if not os.path.exists(os.path.dirname(savepath)):
        os.makedirs(os.path.dirname(savepath))
    try:
        urlretrieve(url,savepath)
        return savepath
    except:
        print('다운로드오류',url)
        return None
def analyze_html(url,root_url):
    savepath=download_file(url)
    #     None인경우??
    html=open(savepath,encoding='utf-8').read()
    links=enum_link(html,url)
    print(links)
    for link_url in links:
        if link_url.find(root_url) ==-1:
            continue

# if __name__=='__main__':
#     url='https://docs.python.org/3.8/library/'
#     analyze_html(url,url)

a='blue green red'
print(a.find('red'))    #11
print(a.find('blue'))   #0
print(a.find('pink'))   #-1