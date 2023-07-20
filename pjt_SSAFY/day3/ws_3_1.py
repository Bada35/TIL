number_of_people = 0

def increase_user():
    global number_of_people # 함수 내부에서 전역 변수를 수정할 때 명시적으로 global 키워드를 사용해야 함
    number_of_people += 1