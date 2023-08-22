N = int(input())  # N:색종이 장수
area = [[0]*1001 for _ in range(1001)]
res = [0] * (N + 1)

for n in range(1, N + 1):
    st_x, st_y, c, r = map(int, input().split())
    for x in range(c):
        for y in range(r):
            res[area[st_x + x][st_y + y]] -= 1
            area[st_x + x][st_y + y] = n
            res[n] += 1

print(*res[1:], sep='\n')