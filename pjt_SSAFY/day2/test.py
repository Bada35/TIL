person = {'name': 'Alice', 'age': 25}

print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for k, v in person.items():
    print(k, v)