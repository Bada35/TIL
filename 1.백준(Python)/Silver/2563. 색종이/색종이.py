import sys
input = sys.stdin.readline

N = int(input())
area = [[0] * 100 for _ in range(100)]
res = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            area[i][j] = 1

for k in area:
    res += k.count(1)
print(res)
