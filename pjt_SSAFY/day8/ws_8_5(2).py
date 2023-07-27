class Dog:
    sound = '멍멍'

    def __init__(self):
        pass

    def __str__(self):
        return f'애완동물은 {self().sound} 소리를 냅니다.'


class Cat:
    sound = '야옹'

    def __init__(self):
        pass

    def __str__(self):
        return f'애완동물은 {self().sound} 소리를 냅니다.'


class Pet(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.\n애완동물은 {Cat.sound} 소리를 냅니다.'
    

pet1 = Pet()
print(pet1)