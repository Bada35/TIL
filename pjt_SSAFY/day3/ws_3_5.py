# ws_3_5.py
number_of_people = 0
number_of_book = 100


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    user_info = {
        'name': name,
        'age': age,
        'address': address
    }
    return user_info


many_user = list(map(create_user, name, age, address))

# info 인자에 사용될 딕셔너리 생성
# 요구사항 1.고객의 이름과 나이만 담도록 함 2.many_user와 map을 사용함 3.map에 사용될 함수는 lambda로 구현함
rental_user = list(map(lambda info: {'name': info['name'], 'age': info['age']}, many_user))


def rental_book(info):
    rental_books = info["age"]//10
    global number_of_book
    number_of_book -= rental_books
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{info["name"]}님이 {rental_books}권의 책을 대여하였습니다.')


list(map(rental_book, rental_user))