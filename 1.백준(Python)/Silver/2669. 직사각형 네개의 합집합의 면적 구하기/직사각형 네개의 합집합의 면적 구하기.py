grid = [[0]*100 for _ in range(100)]

for _ in range(4):
    sx, sy, ex, ey = map(int, input().split())
    for x in range(sx, ex):
        for y in range(sy, ey):
            grid[x][y] += 1

res = 0
for i in grid:
    res += i.count(0)

print(100*100 - res)
