# # import requests
# # from bs4 import BeautifulSoup
# # url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
# # recvd=requests.get(url)
# # # print(recvd)
# # dom=BeautifulSoup(recvd.text,'lxml')
# # lis=dom.find_all('li',{'class':"common_sp_list_li"})
# # # print(len(lis))
# # for li in lis:
# #     # print(li)
# #     pageUrl='https://www.10000recipe.com'+li.find('a')['href']
# #     print(pageUrl)
#
#
# import requests
# from bs4 import BeautifulSoup
# url='https://www.10000recipe.com/recipe/6912734'
# recvd=requests.get(url)
# dom=BeautifulSoup(recvd.text,'lxml')
# title=dom.find('div',class_="view2_summary st3").find('h3').text
# # print(title)
# # 재료
# view_step=dom.find('div',class_='view_step')
# divs=view_step.find_all('div',{'class':"media-body"})
# # print(len(divs))
# # print(divs)
# i=0
# for div in divs:
#     i=i+1
#     print(str(i)+']'+div.text)
#----------------------
import requests
from bs4 import BeautifulSoup
def makeContent(pageUrl):
    recvd=requests.get(pageUrl)
    dom=BeautifulSoup(recvd.text,'lxml')
    title=dom.find('div',class_="view2_summary st3").find('h3').text
    # 재료
    view_step=dom.find('div',class_='view_step')
    divs=view_step.find_all('div',{'class':"media-body"})
    i=0
    contents=[]
    for div in divs:
        i=i+1
        contents.append(str(i)+']'+div.text)
    print('{}\n\n조리순서\n{}'.format(title,'\n'.join(contents)))
def main(url):
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    lis=dom.find_all('li',{'class':"common_sp_list_li"})
    for li in lis:
        pageUrl='https://www.10000recipe.com'+li.find('a')['href']
        # print(pageUrl)
        makeContent(pageUrl)
        break
url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
if __name__=='__main__':
    main(url)


