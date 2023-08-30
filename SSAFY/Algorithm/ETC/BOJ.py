w, h = map(int, input().split())
n = int(input())
dist = []
ans = 0
for _ in range(n+1):
    # 북:1 남:2 서:3 동:4
    a, b = map(int, input().split())
    if a == 1:
        dist.append(2*w + h - b)
    elif a == 2:
        dist.append(b)
    elif a == 3:
        dist.append(2*w + h + b)
    elif a == 4:
        dist.append(w + h - b)

cur = dist[-1]

for i in range(n):
    ans += min(dist[i] - cur, 2 * (w + h) - (dist[i] - cur))

print(ans)