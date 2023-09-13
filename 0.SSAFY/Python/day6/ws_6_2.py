# ws_6_2.py

def get_value_from_dict(input_dict, input_key):
    return input_dict.get(input_key)
    
my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
