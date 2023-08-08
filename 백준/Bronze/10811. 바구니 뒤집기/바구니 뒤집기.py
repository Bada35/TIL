N, M = map(int, input().split())
li = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        li[i-1:j] = li[j-1::-1]
    else:
        li[i-1:j] = li[j-1:i-2:-1]
print(*li)
