# def f1(n):
#     return n * 10
#
#
# # print(f1(5))
# a = f1
#
# # print(type(a))
# # print(a(7))
#
# # 람다 함수 : 메모리 절약, 가독성 향상, 코드 간결
# # lambda 매개변수:반환값
# b = lambda n: n * 10
# print(b(1))
# print('-'*10)
#
#
# def f2(x, y, f):
#     print(x * y * f(x + y))
#
#
# f2(10, 100, lambda n: n+1)

# [3, 6, 9, 12, 15]


# def f3(x):
#     result = []
#     for i in x:
#         result.append(i * 3)
#     return result
#
#
# a = [1, 2, 3, 4, 5]
# print(f3(a))

# map(함수, 반복가능객체) : 매개변수로 함수와 반복가능객체를 입력
#
#
# def f4(x):
#     return x*3
#
#
# print(f4(7))
# print(f4([1, 2, 3])) # 리스트가 3번 반복
# print(map(f4, [1, 2, 3])) # map 객체
# print(list(map(f4, [1, 2, 3])))
# print(list(map(lambda n: n * 4, [1, 2, 3])))

# 파일경로 리눅스, 맥에서는 / , 윈도우 \
# os 모듈 : 디렉토리, 파일 등의 os 자원 제어
# glob 모듈

import os
import glob

# print('현재 작업 디렉토리', os.getcwd()) # current working directory
# print('현재 작업 디렉토리의 목록', os.listdir())
# print('D:\ 목록', os.listdir('d:\\'))
# print(os.listdir('d:\\down\\erd'))
# print(os.path.join('..', 'test1'))
# print(os.listdir(os.path.join('..', 'test1')))
# print(os.path.join('..', 'test1', 'Scripts'))
# print(os.listdir(os.path.join('..', 'test1', 'Scripts')))
#
# # with open('data\\webtoon.csv', 'w', encoding='utf-8') as f:
# with open(os.path.join('data', 'webtoon.csv'), 'w', encoding='utf-8') as f:
#     pass

# # 현재 폴더의 모든 파일 리스트로 반환
# print(glob.glob('*'))
# # 현재 위치의 확장자가 py인 모든 파일 리스트로 반환
# print(glob.glob('*.py'))
# f1 = 'D:\\study\\pj1\\data\\Beauty.smi'
# print(os.path.dirname(f1))
# # 가장 마지막에 있는 이름(파일이든 디렉토리이든)
# print(os.path.basename(f1))

# f = open(os.path.join('data', 'Beauty.smi'))
# # print(f.read())
# # print(f.readline())
# print(f.readlines())
# f.close()

# f = open(os.path.join('data', 'Beauty.smi'))
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end='')
# f.close()

# --data 폴더의 모든 파일 내용 출력--
# filelist = glob.glob(os.path.join('data', '*'))
# # print(filelist)
# for file in filelist:
#     with open(file, encoding='utf-8') as f:
#         print(f.read())
#         print('-' * 30)

# Beauty.smi --> [자막만] --> Beauty.txt


def makeTxt(inputFile):
    f = open(inputFile, encoding='utf-8')
    result = []
    for line in f:
        line = line.replace('\n','')
        if len(line) < 4:
            continue
        elif line.count(':') == 4:
            continue
        line = line.replace('<b>', '')
        line = line.replace('</b>', '')
        line = line.replace('<i>', '')
        line = line.replace('</i>', '')
        result.append(line)
    f.close()
    return result


def makeFile(inputFile, tmp):
    filename = inputFile[:-3]+'txt'
    # print(filename)
    with open(filename, 'w', encoding='utf-8') as fw:
        for t in tmp:
            fw.write(t+'\n')


def main():
    inputFile = 'data\\Beauty.smi'
    tmp = makeTxt(inputFile)
    makeFile(inputFile, tmp)


if __name__ == '__main__':
    main()
