# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'반갑습니다. {self.name}입니다.')


# class Professor(Person):
#     def __init__(self, name, age, department):
#         super().__init__(name, age)
#         self.department = department


# class Student(Person):
#     def __init__(self, name, age, gpa):
#         super().__init__(name, age)
#         self.gpa = gpa


# jisu = Professor('서지수', 30, '전자공학과')
# jisu.talk()



# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greeting(self):
#         return f'안녕, {self.name}'
    

# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'
    

# class Dad(Person):
#     gene = 'XY'

#     def walk(self):
#         return '아빠가 걷기'
    

# class FirstChild(Dad, Mom):
#     mom_gene = Mom.gene

#     def __init__(self, name):
#         super().__init__(name)

#     # def __init__(self, name):
#     #     Mom.__init__(name)  엄마 name 받아오고싶을 경우

#     def swim(self):
#         return '첫째가 수영'
    
#     def cry(self):
#         return '첫째가 응애'
    

# baby1 = FirstChild('아가')
# print(baby1.cry()) # 첫째가 응애
# print(baby1.swim()) # 첫째가 수영
# print(baby1.walk()) # 아빠가 걷기
# print(baby1.gene) # XY
# print(baby1.mom_gene) # XX 쓰고싶으면 이렇게 하는 수밖에

# print(FirstChild.mro())

# try:
#     num = int(input('100으로 나눌 값을 입력하시오 : '))
#     print(100 / num)
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('숫자가 아닙니다.')


