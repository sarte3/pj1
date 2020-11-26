import requests
from bs4 import BeautifulSoup


# def saveImg(imgUrl, title):
#     # print(imgUrl)
#     # print(title)
#     title = title.replace('[','')
#     title = title.replace(']', '')
#     title = title.replace(',', '')
#     title = title.replace("'", '')
#     title = title.replace("?", '')
#     title = title.replace('.', '')
#     filename = 'img\\'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
#     # print(filename)
#     r = requests.get(imgUrl)
#     with open(filename, 'wb') as f:
#         f.write(r.content)
#
#
# def makeData(pageUrl):
#     r = requests.get(pageUrl)
#     # print(r)
#     d = BeautifulSoup(r.text, 'lxml')
#     imgUrl = d.find('div', id='newsEndContents').find('img')['src']
#     title = d.find('h4').text
#     saveImg(imgUrl, title)
#     content = d.find('div', id='newsEndContents').text
#     str = '{}::\n{}'.format(title, content)
#     print(str)
#     # print(imgUrl)
#     # print(str)
#
#     # print(imgUrl)
#     # print(title)
#     # print(content)
#
# url = 'https://sports.news.naver.com/index.nhn'
# recvd = requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom = BeautifulSoup(recvd.text, 'lxml')
# aes = dom.find_all('a', class_='link_today')
# # print(aes)
# for a in aes:
#     pageUrl = 'https://sports.news.naver.com'+a['href']
#     # print(a['href'])
#     # print(pageUrl)
#     makeData(pageUrl)


# 만개의 레시피에서 밑반찬 레시피를 recipe.txt로 저장하세요

def createData(pageUrl):
        r = requests.get(pageUrl)
        d = BeautifulSoup(r.text, 'lxml')
        title = d.find('h3').text
        intro = d.find('div', id='recipeIntro')

        if intro == None :
            intro = ''
        else:
            intro = intro.text
        orders = d.find_all('div', class_='view_step_cont')
        title = title.strip()
        title = title.replace('\n', '')
        intro = intro.strip()
        intro = intro.replace('\n', '')
        strs = '{}::{}::\n'.format(title, intro)

        i = 0
        for order in orders:
            i = i + 1
            order = order.text.replace('\n','')
            strs += str(i) + ')' + order
            strs += '\n'

        return strs


def main(url):
    recvd = requests.get(url)
    dom = BeautifulSoup(recvd.text, 'lxml')
    aes = dom.find_all('a', class_='common_sp_link')
    with open('data\\recipe.txt', 'w', encoding='utf-8') as f:
        for a in aes:
            pageUrl = 'https://www.10000recipe.com/' + a['href']
            strs = createData(pageUrl)
            print(strs)
            f.write(strs)

url = 'https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
if __name__ == '__main__':
    main(url)