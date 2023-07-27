# ws_5_5.py

# 편한대로 구현
# def even_elements(my_list):
#     even_list = []
#     for i in my_list:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list

# extend와 pop 이용하여 구현

# 내방식
# def even_elements(input_list):
#     index = 0
#     while index < len(input_list):
#         if input_list[index] % 2 != 0:
#             input_list.pop(index)
#         else:
#             index += 1
#     input_list.extend([])
#     return input_list

# 교수님방식
def even_elements(numbers):
    result = []
    while numbers:
        number = numbers.pop



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
