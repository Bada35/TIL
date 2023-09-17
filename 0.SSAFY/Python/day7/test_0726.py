# # 클래스 정의
# class Person:
#     pass

# # 인스턴스 생성
# iu = Person()

# # 메서드 호출
# iu.메서드() # -> 생략되어있지만 사실 Person클래스에 정의되어있음

# # 속성(변수) 접근
# iu.attribute

# # 클래스 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'

#     # 메서드
#     def __init__(self, name):
#         self.name = name

#     def singing(self):
#         return f'{self.name}가 노래합니다.'
    
# # 인스턴스 생성
# singer1 = Person('iu')
# singer2 = Person('BTS')

# # 메서드 호출
# print(singer1.singing())
# print(singer2.singing())

# # 속성(변수) 사용
# print(singer1.blood_color)
# print(singer2.blood_color)


# name = 'jisu' # str의 객체 'jisu'

# {
#     'caffein' : 0,
#     'coffe' : drink_coffee
# }

# def drink_coffee():
#     caffein += 10




# # 객체 붕어빵1, 2, 3
# 붕어빵1 : {
#     생김새 : 봉어모양,
#     재료 : 팥
# }

# 붕어빵2 : {
#     생김새 : 봉어모양,
#     재료 : 팥
# }

# 붕어빵3 : {
#     생김새 : 붕어모양,
#     재료 : 슈크림
# }

# #... 이렇게 계속 붕어빵을 찍어내긴 힘듦
# #그래서 class를 만드는것

# class 붕어빵틀(): # class는 생성자함수
#     생김새 : 붕어모양

#     def __init__(self,재료):
#         self.재료 = 재료

# 붕어1 = 붕어빵틀(팥)
# 붕어2 = 붕어빵틀(팥)
# 붕어3 = 붕어빵틀(슈크림)

# # 붕어1은 객체다
# # 붕어1은 클래스 붕어빵틀의 인스턴스이다



# me = {
#     'caffein' : 100,
#     'coffee' : drink_coffee,
#     'greeting' : greet
# }

# # 객체의 상태를 바꾸기 때문에 인스턴스 메서드
# def drink_coffee():
#     coffein += 10

# # 객체의 상태를 바꾸지 않기 때문에 스태틱 메서드
# def greet():
#     print("좋은 아침입니다!")


# class Person:
#     name = 'unknown'

#     def talk(self):
#         print(self.name)

# p1 = Person()
# p1.talk() # unknown

# # p2 인스턴스 변수 설정 전/후
# p2 = Person()
# p2.talk() # unknown
# p2.name = 'Kim'
# p2.talk() # Kim

# print(Person.name) # unknown
# print(p1.name) # unknown
# print(p2.name) # Kim



# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

# person1 = Person('IU')
# person2 = Person('BTS')

# print(Person.count) #2


# class Circle():
#     pi = 3.14

#     def __init__(self, r):
#         self.r = r

# c1 = Circle(5)
# c2 = Circle(10)


# print(Circle.pi) # 3.14
# print(c1.pi)     # 3.14

# Circle.pi = 5
# print(c2.pi) # 5

# c2.pi = 5 # 인스턴스 변수 변경
# print(Circle.pi) # 3.14 (클래스 변수)
# print(c1.pi) # 3.14 (클래스 변수)
# print(c2.pi) # 5 (새로운 인스턴스 변수가 생성됨)



# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

#     @classmethod
#     def number_of_population(cls):
#         print(f'인구수는 {cls.count}입니다.')

# person1 = Person('iu')
# person2 = Person('BTS')

# Person.number_of_population() # 인구수는 2입니다.


# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r
    
#     def __str__(self):
#         return f'[원] radius: {self.r}'
    
# c1 = Circle(10)
# c2 = Circle(1)

# print(c1) # [원] radius: 10
# print(c2) # [원] radius: 1


a = 3.2 - 3.1
b = 1.2 - 1.1
print(a,b)