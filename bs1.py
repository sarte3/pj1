# import bs4
import requests
# 서버에 접근
# url = 'https://www.naver.com'
# recvd = requests.get(url)
# 접근 결과 코드
# print(recvd)
# html 코드
# print(recvd.text)
# print(recvd.encoding)
# print(recvd.headers)


from bs4 import BeautifulSoup
# 웹페이지에 접근하여 태그 인식

f = open('data\\test.html', encoding='utf-8').read()
# print(f)

# BeautifulSoup(웹페이지, 파싱방식)
# 파싱 : html.parser, html5lib, lxml
# dom = BeautifulSoup(f, 'html.parser')
# dom : document object model
dom = BeautifulSoup(f, 'lxml')
# print(dom)

# 특정 첫번째 tag 가져오기
# dom.find('태그')
# dom.태그
# div = dom.div
# print(div)

# dom.find_all('태그') 모든 태그 추출, 리스트로 반환
# div = dom.find('div')

# divs = dom.find_all('div')
# print(divs) # [div, div, ...] 리스트로 반환됨

# firstdiv = dom.div
# div2 = firstdiv.div
# # print(div2)
# ps = div2.find_all('p')
# print(ps)

# dom.find('태그', class_='클래스명')
# dom.find(class_='클래스명')
# cl = dom.find('div', class_='ex_class')
# cl = dom.find(class_='ex_class')
# cl = dom.find('div', {'class': 'ex_class'})
# print(cl)

# dom.find('태그', {'class':'클래스명'})
# dom.find_all(class_='클래스명')
# dom.find_all('태그', {'class':'클래스명'})

# exs = dom.find_all('div', class_='ex_class')
# exs = dom.find_all(class_='ex_class')
# exs = dom.find_all('div', {'class': 'ex_class'})
# exs = dom.find_all('div', {'class': 'ex_class'})

# print(exs)

# 클래스가 sister인 모든 태그
# sisters = dom.find_all(class_='sister')
# print(sisters)

# id가 third인 태그
thirds = dom.find_all(id='third')
# print(third)

# id가 third인 모든 태그의 첫 번째 p 태그
# a = ['one']
# print(a[0])
# b = 'one'
# print(b)
print('-'*30)
p1 = thirds[0].find('p')
print(p1)

# import, main()