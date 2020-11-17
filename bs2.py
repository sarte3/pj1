from bs5 import BeautifulSoup
with open('data\\test.html', mode='r', encoding='utf-8') as f:
    txt = f.read()
    # print(txt)
    # print(type(txt))

    dom = BeautifulSoup(txt, 'lxml')
    # print(dom)
    # div = dom.find('div') # div인 첫번째 태그
    # print(div)
    # divs = dom.find_all('div') # div인 모든 태그
    # print(divs)
    # ids = dom.find(id='ex_id')
    # print(ids)
    # div 태그중에 클래스가 'ex_class'인 것 첫 번째
    # divs = dom.find('div', {'class': 'ex_class'})
    # print(divs)
    # div 태그 중에 클래스가 'ex_class'인 것 모두 추출
    # divs = dom.find_all('div', {'class': 'ex_class'})
    # # 클래스가 'ex_class'인 것 모두 추출
    # divs = dom.find_all(class_='ex_class')
    # print(divs)

    # id가 'ex_id'인 것 추출
    # ids = dom.find(id='ex_id')
    # # print(ids)
    # # id가 'ex_id'인 것 중 모든 p 태그 추출
    # ps = ids.find_all('p')
    # print(ps)

    # data 추출
    # dom.string
    # dom.text
    # dom.get_text()

    # 속성 추출
    # dom['속성']
    # dom.get('속성')
    # dom.attrs['속성']

    # title = dom.find('title')
    # print(title)
    # print(title.string)
    # print(title.text)
    # print(title.get_text())
    #
    # a = dom.find_all('a') # list
    # for i in a:
    #     print(i.text)
    #     print(i['href'])

    # id가 link2인 요소의 class 추출
    # print(dom.find(id='link2').get('class'))

    # DOM 추적
    # dom.parent 부모
    # dom.parents 조상, 객체로 반환
    # dom.children 자식
    # dom.descendants 자손
    # dom.next_siblings 아래쪽 형제 요소
    # dom.previous_siblings 위쪽 형제 요소

    # title = dom.find('p', class_='title')
    # # print(title)
    # # print('parent :', title.parent)
    # # print('-'*30)
    # # print('parents : ', title.parents)
    #
    # for p in title.parents:
    #     print(p)
    #     print('-' * 30)

    # id가 second인 div
    # div = dom.find(id='second')
    # print(div)
    # divchild = div.children
    # print('-'*30)
    # print(divchild) # list 객체 반환
    # for c in divchild:
    #     print(c)
    #     print('!'*30)

    # divdes = div.descendants;
    # print(divdes)
    # print('-'*30)
    #
    # for d in divdes:
    #     print(d)
    #     print('!'*30)

    # id가 link2인 a의 형제 찾기
    a = dom.find(id='link2')
    print(a)
    anext = a.next_siblings
    print(anext)

    for temp in anext:
        print(temp)
        print('$'*30)
