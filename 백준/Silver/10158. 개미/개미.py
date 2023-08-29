t = [list(map(int, input().split())) for _ in range(3)]

print(*t, sep='\n')

y = list(map(list, zip(*t[::-1])))
# for i in range(len(y)):
#     y[i] = list(y[i])

print(*y, sep='\n')