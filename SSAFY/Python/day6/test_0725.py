#  # .add(x) : 세트에 x를 추가
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set) # {1, 2, 3, 4}

# my_set.add(4)
# print(my_set) # {1, 2, 3, 4} 세트라 중복값 추가x

# # .clear() : 세트의 모든 항목 제거
# my_set1 = {1, 2, 3}
# my_set1.clear()
# print(my_set1) # set(x)

# # .remove() : 세트에서 항목 x를 제거
# my_set2 = {1, 2, 3}
# my_set2.remove(2)
# print(my_set2) # {1, 3}

# my_set2.remove(10) # KeyError

# # .discard() : remove와 같지만 없는값 삭제할때 error없음
# my_set3 = {1, 2, 3}
# my_set3.discard(10) # None(에러 일어나지 않음)

# # .pop()  : 세트에서 임의의 요소를 제거하고 반환
# my_set4 = {1, 2, 3}
# element = my_set4.pop()

# print(element) # 1
# print(my_set4) # {2, 3}


# # Hash Table
# print(hash(1)) # 1
# print(hash('삼계탕')) # 계속 바뀌는 주소값


# my_set = {1, 2, 3, 39, 100, 4}
# print(my_set)  # 계속 {1, 2, 3, 100, 4, 39} 똑같이 나옴

# my_str_set = {'a', 'b', 'c', 'd', 'e'}
# print(my_str_set.pop())

# # .update(iterable) : 세트에 다른 iterable 요소를 추가
# my_set5 = {1, 2, 3}
# my_set5.update([4, 5, 1])
# print(my_set5) # {1, 2, 3, 4, 5}

# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 100, 7, 9, 39}

# print(set1.difference(set2)) # {0, 2, 4}
# print(set1.intersection(set2)) # {1, 3}
# print(set1.issubset(set2)) # False
# print(set1.issuperset(set2)) # False
# print(set1.union(set2)) # {0, 1, 2, 3, 4, 100, 7, 39, 9}

# # .clear() : 딕셔너리 D의 모든 키/값 쌍 제거
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person)  # {}

# # .get(key[,default]) : 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
# person = {'name': 'Alice', 'age': 25}

# print(person.get('name'))  # Alice
# print(person.get('country'))  # None
# print(person.get('country', 'Unknown'))  # 키가 없을경우 Unknown 반환

# # ['key'] vs .get('key)
# m_dict = {
#     'name' : 'JISU'
# }

# print(m_dict['name']) # JISU
# print(m_dict.get('name')) # JISU

# # 찾고자하는 키가 없을 때
# print(m_dict['age']) # KeyError
# print(m_dict.get('age')) # None
# print(m_dict.get('age', '몰라')) # 몰라


# # .keys() : 딕셔너리 키를 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.keys())  # dict_keys(['name', 'age’])

# for k in person.keys():
#     print(k) # name age


# #.values() : 딕셔너리 값을 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}
# print(person.keys())  # dict_keys(['name', 'age’])

# for v in person.values():
#     print(v) # Alice 25

# #.items() : 딕셔너리 키/값 쌍을 모은 객체를 반환
# person = {'name': 'Alice', 'age': 25}

# print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
# for k, v in person.items():
#     print(k, v)
# """
# name Alice
# age 25
# """
# # .pop(key[,default]) : 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default 를 반환)
# person = {'name': 'Alice', 'age': 25}

# print(person.pop('age'))  # 25
# print(person)  # {'name': 'Alice'}
# print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError

# #.setdefault(key[,default]) : 키와 연결된 값을 반환
# # 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
# person = {'name': 'Alice', 'age': 25}

# print(person.setdefault('country', 'KOREA'))  # KOREA
# print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# #.update([other]) : other가 제공하는 키/값 쌍으로 딕셔너리를 갱신. 기존 키는 덮어씀
# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}

# person.update(other_person)
# print(person)  # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

# person.update(age=50)
# print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female'}

# person.update(country='KOREA')
# print(person)  # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}


# 혈액형 인원수 세기
# 결과 => {;A;: 3, 'B': 3, 'O': 3, 'AB': 3}

blood_types = {'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'}

#1 []
new_dict = {}
for blood_type in blood_types :
    if blood_type in new_dict:
        new_dict[blood_type] += 1
    else :
        new_dict[blood_type] = 1
print(new_dict)


#2 .get()
new_dict = {}
for blood_type in blood_types :
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
print(new_dict)

#3 .setdefault()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)