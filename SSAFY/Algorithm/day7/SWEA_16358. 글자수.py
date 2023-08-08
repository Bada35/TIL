T = int(input())
for tc in range(1, T + 1):
    s1 = set(map(str, input()))
    s2 = list(map(str, input()))
    mx = []
    for s in s1:
        mx.append(s2.count(s))
    print(f'#{tc} {max(mx)}')