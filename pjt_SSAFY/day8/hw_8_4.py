# hw_8_4.py

class UserInfo:
    name = None
    age = None

    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):

        self.name = input('이름을 입력하세요 : ') # 이름은 숫자로 입력해도 그 자체가 이름일 수 있음

        try:
            self.age = int(input('나이를 입력하세요 : '))
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')


    def display_user_info(self):
        if self.name != None and self.age != None: # name이랑 age둘 다 None이 아니라면
            print(f'사용자 정보 :\n이름 : {self.name}\n나이 : {self.age}')
        else:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
