# hw_6_4.py

def add_item_to_dict(input_dict, input_key, input_value):
    input_dict.setdefault(input_key,input_value)
    return input_dict

my_dict = {'name' : 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
