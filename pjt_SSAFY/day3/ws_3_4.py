number_of_people = 0
user_info = []

def increase_user():
    global number_of_people  # 함수 내부에서 전역 변수를 수정할 때 명시적으로 global 키워드를 사용해야 함
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = list(map(create_user, name, age, address))
print(user_list)
