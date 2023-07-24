# ws_5_3.py

# 내 방법
# def sort_tuple(new_tuple):
#     new_list = list(new_tuple)
#     new_list.sort()
#     new_tuple = tuple(new_list)
#     return new_tuple

def sort_tuple(new_tuple):
    return tuple(sorted(list(new_tuple)))


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
