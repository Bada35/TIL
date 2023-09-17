N, M = map(int, input().split())
li = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for r in range(i-1, j):
        li[r] = k
print(*li)