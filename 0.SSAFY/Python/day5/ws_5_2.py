# ws_5_2.py

# 내 방법(동작은 함)
# def remove_duplicates(new_lst):
#     new_set = set(new_lst)
#     new_lst = list(new_set)
#     return new_lst

#chat GPT 방법
def remove_duplicates(new_lst):
    return list(set(new_lst))

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
