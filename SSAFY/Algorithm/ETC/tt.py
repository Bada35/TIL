from itertools import combinations

s = {'o', 'e', 'h', 'l', 'r'}
for i in combinations(s, 3):
    print(i)