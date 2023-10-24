
def func(input1, *args):
    total = 0
    for i in args:
        total += i * 100
    return input1 + total

num1, *num_list, num2 = range(3, 8)
result = func(num1, *num_list)
print(result) # 1503


def change_string(my_string):
    result = ''
    for char in my_string:
        result = char + result
    return result

output = change_string("Hello, world~")
print(output)


# func(0)이 호출되는 횟수는?
def func(n):
    if n==0 or n==1:
        return 1
    else:
        return func(n-1) + func(n-2)
    
func(4)


# [서술형]
my_list = [1,2,3,4,5,6,7]
print(my_list[-1:-4]) # []
