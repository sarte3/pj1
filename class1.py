# class 클래스명:
#     메서드
#     메서드
# class Car:
#     def __init__(self, t, c):
#         print('생성자')
#         self.type = t
#         self.color = c
#
#     def __del__(self):
#         print('소멸자')
#
#     def showInfo(self):
#         print(self.type+', '+self.color)
#
#     def tuning(self, c):
#         self.color = c
#         self.showInfo()
#
#
# c1 = Car('suv', '은색')
# # c2 = Car()
# c1.showInfo()
# c1.tuning('검은색')

# 다중 상속
# class X(object):
#     pass
#
#
# class Y:
#     pass
#
#
# class Z():
#     pass
#
#
# # print('상속관계 확인 : ', X.mro())
# # print('상속관계 확인 : ', Y.mro())
# # print('상속관계 확인 : ', Z.mro())
#
#
# class A(X, Y):
#     pass
#
#
# class B(Y, Z):
#     pass
#
#
# class D(A, B, Z):
#     pass
#
#
# print('상속관계 확인 : ', A.mro())
# print('상속관계 확인 : ', D.mro())
# 너무 복잡한 다중상속은 코드 해석이 어렵다
# class Car:
#     def __init__(self, type, color):
#         self.type = type
#         self.color = color
#
#     def show(self):
#         print('Car class show 메서드', self.type, self.color)
#
#
# class KiaCar(Car):
#     def __init__(self, carname, type, color):
#         # 부모 생성자 호출
#         super().__init__(type, color)
#         self.carname = carname
#
#     def show(self):
#         print('KiaCar class show 메서드', self.type, self.color, self.carname)
#
#     def tuning(self, color):
#         self.color = color
#
#
# class HyundaiCar(Car):
#     def __init__(self, carname, type, color):
#         super().__init__(type, color)
#         self.carname = carname
#
#
# k1 = KiaCar('k9', '세단', '흰색')
# k1.show()
# k1.tuning('노랑')
# # 인스턴스 메서드 호출
# k1.show()
# # 인스턴스 속성 접근
# print(k1.carname)
#
# h1 = HyundaiCar('제네시스', '세단', '비둘기색')
# h1.show()
#
# import cx_Oracle
#
#
# class DBManager:
#     def __init__(self):
#         self.con = cx_Oracle.connect('happy/day@localhost:1521/xe')
#         self.cur = self.con.cursor()
#         print('연결 성공')
#
#     def __del__(self):
#         print('연결 해제')
#         self.con.close()
#
#     def selectAll(self):
#         sql = "select * from webtoon order by no"
#         self.cur.execute(sql)
#         rows = self.cur.fetchall()
#         for row in rows:
#             print(row[0], row[1], row[2], row[3])
#
#     def selectRating(self, rating):
#         sql = "select * from webtoon where rating>={}"
#         self.cur.execute(sql.format(rating))
#         rows = self.cur.fetchall()
#         for row in rows:
#             print(row[0], row[1], row[2], row[3])
#
#     def insert(self, title, rating, regdate):
#         sql = "insert into webtoon values(webtoon_seq.nextval, '{}', '{}', '{}')"
#         self.cur.execute(sql.format(title, rating, regdate))
#         self.con.commit()
#
#     def updateRegdate(self, rating, regdate):
#         sql = "update webtoon set regdate='{}' where rating>={}"
#         self.cur.execute(sql.format(regdate, rating))
#         self.con.commit()
#
#     def deleteRating(self, rating):
#         sql = "delete from webtoon where rating>={}"
#         self.cur.execute(sql.format(rating))
#         self.con.commit()
#
#
# d1 = DBManager()
# d1.insert('둘리', '4.9999', '1990.01.01')
# d1.selectAll()
# d1.selectRating(9.93)
# d1.updateRegdate(9.5,'2020.11.25')
# d1.deleteRating(9.93)
# d1.selectAll()

color = ['red', 'green', 'blue']
fruit = ['apple', 'orange', 'tomato', 'melon']
number = ['one', 'two', 'three']
# for t in zip(color, fruit):
#     print(t)
# for t in zip(color, fruit, number):
#     print(t)
# for c, f, n in zip(color, fruit, number):
#     print(c, f, n)


import cx_Oracle


class DBManager:
    def makeDictFactory(self, cur):
        # print('self.cur.description', self.cur.description)
        # for colinfo in self.cur.description:
        #     colinfo[0]
        colnames = [colinfo[0] for colinfo in self.cur.description]
        templist = []
        for datas in cur.fetchall():
            temp = {}
            for k, v in zip(colnames, datas):
                temp[k] = v
            templist.append(temp)
        return templist

        # def createRow(*arg):
        #     print('createRow() 함수')
        #     print(arg)
        # return createRow()

    def __init__(self):
        self.con = cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur = self.con.cursor()
        print('연결 성공')

    def __del__(self):
        print('연결 해제')
        self.con.close()

    def selectAll(self):
        sql = "select * from webtoon order by no"
        self.cur.execute(sql)
        result = self.makeDictFactory(self.cur)
        for row in result:
            print(row['NO'], row['TITLE'], row['RATING'], row['REGDATE'])

    def selectRating(self, rating):
        sql = "select * from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        result = self.makeDictFactory(self.cur)
        for row in result:
            print(row['NO'], row['TITLE'], row['RATING'], row['REGDATE'])

    def insert(self, title, rating, regdate):
        sql = "insert into webtoon values(webtoon_seq.nextval, '{}', '{}', '{}')"
        self.cur.execute(sql.format(title, rating, regdate))
        self.con.commit()

    def updateRegdate(self, rating, regdate):
        sql = "update webtoon set regdate='{}' where rating>={}"
        self.cur.execute(sql.format(regdate, rating))
        self.con.commit()

    def deleteRating(self, rating):
        sql = "delete from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        self.con.commit()


d1 = DBManager()
# d1.selectAll()
d1.selectRating(9.8)