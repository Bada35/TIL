import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
length = (w + h) * 2
loca = []
res = 0

# 북:1 남:2 서:3 동:4
for _ in range(n + 1):
    di, i = map(int, input().split())
    if di == 2:
        tmp = i
    elif di == 4:
        tmp = w + (h - i)
    elif di == 1:
        tmp = w + h + (w - i)
    else:
        tmp = length - (h - i)
    loca.append(tmp)

dong = loca.pop()

for loc in loca:
    tmp = abs(dong - loc)
    res += min(tmp, length - tmp)

print(res)
