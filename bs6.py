# 영화제목, 점수, 예매율, 상영시간을 추출하여 movie.csv 저장
# 영화 포스터는 img폴더에 저장
from bs4 import BeautifulSoup
import requests

with open('data\\movie.txt', 'w', encoding='utf-8') as f:
    recvd = requests.get('https://movie.naver.com/movie/running/current.nhn')

    dom = BeautifulSoup(recvd.text, 'lxml')
    li = dom.find('ul', class_='lst_detail_t1').find_all('li')
    for l in li:
        title = l.find('dt', class_='tit').find('a').text
        rating = l.find('div', class_='star_t1').find('span', class_='num').text
        book = ''

        if l.find('div', class_='b_star') == None :
            book = ''
        else:
            book = l.find('div', class_='b_star').find('span', class_='num').text
        runTime = l.find('dl', class_='info_txt1').find('span', class_='split').next_sibling
        runTime = runTime.strip()
        imgUrl = l.find('div', class_='thumb').find('img')['src']

        filename = 'img\\' + title + '.jpg'
        # print(filename)

        r = requests.get(imgUrl)

        with open(filename, 'wb') as f1:
            f1.write(r.content)

        f.write('{},{},{},{}\n'.format(title, rating, book, runTime))






