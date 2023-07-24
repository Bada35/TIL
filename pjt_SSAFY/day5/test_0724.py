# print(help(str))

# # 문자열 메서드 예시
# print('hello'.capitalize())  # Hello

# # 리스트 메서드 예시
# numbers = [1, 2, 3]
# numbers.append(4)

# print(numbers) # [1, 2, 3, 4]

# #.find(x) : x의 첫번째 위치 반환 / 없으면 -1 반환
# print('banana'.find('a')) # 1
# print('banana'.find('z')) # -1

# # .index(x) : find()와 같지만 없을경우 오류 발생
# print('banana'.index('a')) # 1
# print('banana'.index('z')) # ValueError : substring not found

# # .isupper(x) / .islower(x) : 대소문자 여부
# string1 = 'HELLO'
# string2 = 'Hello'
# print(string1.isupper()) # True
# print(string2.isupper()) # False
# print(string1.islower()) # False
# print(string2.islower()) # False

# # .isalpha(x) : 유니코드상 Letter 여부
# string3 = 'Hello'
# string4 = '123'
# string5 = '안녕'
# print(string3.isalpha()) # True
# print(string4.isalpha()) # False
# print(string5.isalpha()) # True



# # .replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 변환
# text = 'Hello, world!'
# new_text = text.replace('world', 'Python')
# print(new_text) # Hello, Python!

# # .strip([chars]) : 문자열의 시작과 끝에 있는 공백or지정한 문자 제거
# text = '    Hello, world    '
# new_text = text.strip()
# print(new_text) # 'Hello, world!'

# #★ .split(sep=None, maxsplit=-1) : 지정한 문자를 구분자로 문자열 분리 -> 문자열 리스트로 변환
# text2 = 'Hello, world!'
# words = text2.split(',')
# print(words) # ['Hello', ' world!']

# #★ 'seperator'.join([iterable]) : split의 반대
# # iterable 요소들을 지정한 문자열을 구분자로 이용하여 하나의 문자열로 연결
# words = ['Hello', 'world!']
# text3 = '-'.join(words)
# print(text3) # 'Hello-world!'

# # 나머지
# text4 = 'heLLo, woRld!'
# print(text4.capitalize()) # Hello, world!
# print(text4.title())      # Hello, World!
# print(text4.upper())      # HELLO, WORLD!
# print(text4.swapcase())   # HEllO, WOrLD!

# #메서드는 이어서 사용 가능(chained)
# print(text4.swapcase().replace('l', 'z')) # HEzzO, WOrLD!


# # ★ .append(x) vs .extend(iterable)
# numbers = [1, 2, 3]
# numbers2 = [4, 5, 6]

# print(numbers.append(numbers2)) # None 이 메서드들은 복사본 반환X 원본을 바꿈
# numbers.append(numbers2)
# print(numbers) # [1, 2, 3, [4, 5, 6]]
# numbers.extend(numbers2)
# print(numbers) # [1, 2, 3, 4, 5, 6]

# # .insert(i, x) : 리스트의 지정한 인덱스 위치 i 에 항목 x 삽입
# my_list = [1, 2, 3]
# print(my_list.insert(1, 5)) # None
# print(my_list) # [1, 5, 2, 3]

# #. remove(x) : 리스트에서 첫 번째로 일치하는 항목 삭제
# my_list2 = [1, 2, 3, 4, 2]
# my_list2.remove(2)
# print(my_list2) # [1, 3, 4, 2] 첫 번째 일치항목만 삭제

# # ★.pop(i) : 리스트에서 지정한 인덱스(지정x일경우 마지막) 항목을 제거하고 "반환"
# # .append() 반대
# my_list3 = [1, 2, 3, 4, 5]
# item1 = my_list3.pop()
# item2 = my_list3.pop(2)
# print(item1) # 5
# print(item2) # 3
# print(my_list3) # [1, 2, 4]

# # .clear : 리스트 비우고 싶을때



# # .index(x, start, end) : 리스트에서 첫 번째로 일치하는 항목 인덴스 반환.
# # !!값 반환이 아닌 "인덱스" 반환한다는 점 주의!!
# my_list = [1, 2, 3]
# print(my_list.index(2)) # 1

# # .count(x) : 리스트에서 항목x가 등장하는 횟수 반환
# my_list2 = [1, 2, 2, 3, 2]
# print(my_list2.count(2)) # 3

# # .sort(reverse=False) : 원본 리스트 오름차순으로 정렬. 반환X
# my_list3 = [3,1,2]
# my_list3.sort()
# print(my_list3) # [1,2,3]
# my_list3.sort(reverse=True)
# print(my_list3) # [3,2,1]

# # .reverse() : 리스트의 순서 역순으로 변경.
# my_list4 = [1, 3, 2, 4]
# my_list4.reverse()
# print(my_list4) # [4, 2, 3, 1] 정렬X !!reverse는 역순으로 정렬하는것이다(x) 낚이지X!!


# # .sort() vs sorted()
# numbers1 = [3, 2, 1]
# numbers2 = [3, 2, 1]

# print(numbers1.sort()) # None
# print(sorted(numbers2)) # [1, 2, 3]

# print(numbers1) # [1, 2, 3]
# print(numbers2) # [3, 2, 1]

# numbers = [1, 2, 3]

# # 1.할당
# list1 = numbers

# # 2.슬라이싱
# list2 = numbers[:]

# numbers[0] = 100
# print(list1) # [100, 2, 3]
# print(list2) # [1, 2, 3]


#1.값에 의한 복사
a = 1
b = a
a = 2
print(a,b) # 2 1


#2.참조에 의한 복사
c = [1,2]
d = c
c[0] = 10
print(c,d) # [10, 2] [10, 2]


#3.얕은 복사(Shallow copy)
e = [1,2]
f = e[:]
e[0] = 100
print(e,f) # [100, 2] [1, 2]

g = [5,6,[7,8,9]]
h = g[:]
g[2][0] = 700
print(g,h) # [5, 6, [700, 8, 9]] [5, 6, [700, 8, 9]]


#4. 깊은 복사(Deep copy)
import copy

i = [5,6,[7,8,9]]
k = copy.deepcopy(i)
i[2][0] = 700
print(i,k) # [5, 6, [700, 8, 9]] [5, 6, [7, 8, 9]]

