# # ws_5_5.py

# # extend와 pop 이용하여 구현
# def even_elements(my_list):
#     even_list = []
#     even = []
#     for i in range(len(my_list)):
#         if i % 2 == 0:
#             even = list(my_list.pop(i))
#             my_list.extend(even)
#     return even_list


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list.pop(i))