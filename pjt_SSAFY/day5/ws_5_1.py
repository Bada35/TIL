# ws_5_1.py

def reverse_string(input_str):
    return ''.join(reversed(input_str))
# reversed는 자료형과 주소를 반환하기 때문에 ''.join을 붙여줘야함   

result = reverse_string("Hello, World!")
print(str(result))
