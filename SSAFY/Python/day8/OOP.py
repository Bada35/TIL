# 캡슐화
class Student():
    def __init__(self, name, age, id, grade):
        self.name = name
        self.age = age
        self.id = id
        self.__grade = grade

    def grade(self): # getter함수 게터함수
        return self.__grade

Lee = Student('Lee', 24, '2020111423', 4.3)

print(Lee.name)
print(Lee.age)
print(Lee.id)
# print(Lee.grade)
# Lee.grade = 4.5
# print(Lee.grade)

grade = Lee.grade()
print(grade)


# 다형성
class Animal():
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("울음소리")

class Cat(Animal):
    def bark(self):
        return '냐옹'
    
class Dog(Animal):
    def bark(self):
        return "멍멍"
    
cat = Cat('나비')
dog = Dog('누렁이')

cat.bark() # 냐옹
dog.bark() # 멍멍


# 추상화
class Person():
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def walk(self):
        return f'{self.name}은 걷는다.'