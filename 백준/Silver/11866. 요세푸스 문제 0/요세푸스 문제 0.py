N, K = map(int, input().split())
p = [i for i in range(1, N + 1)]
tmp = 1
res = []
while p:
    length = len(p)
    tmp += K - 1
    while tmp > length:
        tmp -= length
    res.append(p.pop(tmp - 1))

print(f"<{', '.join(map(str, res))}>")

