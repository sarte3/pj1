# open('파밀명',모드)
# 사용
# 변수.close() 자원 반납
# 모드 : r(읽기), w(쓰기), a(추가)

# f = open('d:\study\pj1\data\poem.txt', 'r', encoding='UTF-8')
# f = open('data\poem.txt', encoding='UTF-8')
# # txt = f.read() #전체 내용 읽기
# txt = f.read(5) # 5글자 읽기
#
# print(txt)
# print(type(txt))
# f.close()

# print('-'*30)
#
# f = open('data\\poem.txt', encoding='utf-8')
# txt = f.readline() # 한 줄 읽기
# print(txt)
# print(type(txt)) # 문자열
# f.close()

# print('-'*30)
#
# f = open('data\\poem.txt', encoding='utf-8')
# txt = f.readlines() # 줄단위 리스트 반환
# print(txt)
# print(type(txt)) # 문자열
#
# for line in txt:
#     print(line.strip())
#
# f.close()

# print('-'*30)
# # with open('파일명, 모드) as 변수명:
# # with 블럭이 끝날 때 자동 close
# with open('data\\poem.txt', encoding='utf-8') as f:
#     txt = f.read()
#     print(txt)

# print('-'*30)
#
# with open('data\\test1.txt', 'w', encoding='utf-8') as f:
#     f.write('very nice day!!!\n')
#     f.write('홍준씨 연락왔어요?')

# print('-'*30)

# with open('data\\test2.txt', mode='a', encoding='utf-8') as f:
#     for i in range(100):
#         f.write(str(i)+'\n')
# print('-'*30)

# fruit = ['사과', '배', '포도']
# with open('data\\test2.txt', 'a', encoding='utf-8') as f:
#     # for a in fruit:
#     #     f.write(a)
#     f.writelines(fruit) # 리스트를 파일에 쓰기

# with open('data\\test1.txt', 'w') as f:
#     # 파일로 출력
#     print('test print', file=f)

# print('-'*30)
#
# col = ['이름', '나이', '주소']
# names = ['홍길동', '심청', '이몽룡', '성춘향']
# age = [20, 16, 16, 16]
# juso = ['서울', '서산', '남원', '진주']
#
# with open('data\\addr.txt', 'w', encoding='utf-8') as f:
#     # ','.join(list) list의 문자열을 ',' 단위로 연결
#     f.write(','.join(col)+'\n')
#     for i in range(len(names)):
#         str = '{}, {}, {}\n'.format(names[i], age[i], juso[i])
#         f.write(str)
#
# print('-'*30)
# a = ['one', 'two', 'three']
# # '연결문자'.join(리스트 or 튜플)
# print('-'.join(a))
# print('?'.join(a))
# print(type('?'.join(a)))
#
# b = ('one', 'two', 'three')
# print('-'.join(b))

print('-'*30)

# 이미지 저장
# <img src="https://movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg">

# 웹 서버에 접근하는 모듈
import requests

url = 'https://movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg'
recvd = requests.get(url)
# 200 확인
print(recvd)

with open('img\\movie.jpg', 'wb') as f:
    # b: binary
    f.write(recvd.content)
