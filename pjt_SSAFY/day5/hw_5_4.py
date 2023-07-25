# main.py

def find_min_max(input_lst):
    input_lst.sort()
    output_lst = [input_lst[0], input_lst[len(input_lst)-1]]
    return tuple([input_lst[0], input_lst[len(input_lst)-1]])

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
