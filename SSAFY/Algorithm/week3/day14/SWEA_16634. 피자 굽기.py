def cook(q, p):
    while len(q) > 1:
        for i in range(len(q)):
            q[i][1] //= 2
            if not q[i][1]:
                q[i] = p.pop(0) if p else q.pop(i)
                break
    return q[0][0]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    piz = [[i + 1, c] for i, c in enumerate(list(map(int, input().split())))]
    Q = piz[:N].copy()

    print(f'#{tc} {cook(Q, piz[N:])}')