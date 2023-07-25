def even_elements(input_list):
    index = 0
    while index < len(input_list):
        if input_list[index] % 2 != 0:
            input_list.pop(index)
        else:
            index += 1
    input_list.extend([])

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_elements(sample_list)
print(sample_list)