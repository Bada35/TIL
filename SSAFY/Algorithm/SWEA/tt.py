
# st = input().split()
# lst1 = st[::4]
# lst2 = st[1::4]
# lst3 = st[2::4]
# lst4 = st[3::4]


st = [int(s) if s.isdigit() else s for s in input().split()]

num_of_elements = len(st) // 4
lst1, lst2, lst3, lst4 = [], [], [], []

for i in range(0, len(st), 4):
    lst1.append(st[i])
    lst2.append(st[i+1])
    lst3.append(st[i+2])
    lst4.append(st[i+3])

print(lst1, lst2, lst3, lst4, sep='\n')
