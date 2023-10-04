lst = []
tc = int(input())

for _ in range(tc):
    tmp = input()
    lst.append((tmp, len(tmp)))

lst.sort(key=lambda x: (x[1], x[0]))

print(lst[0][0])

for i in range(1, tc):
    if lst[i][0] != lst[i-1][0]:
        print(lst[i][0])