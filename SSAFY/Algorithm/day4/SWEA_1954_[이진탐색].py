#    ↓   ←   ↑  →
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    sn = [[0] * N for _ in range(N)]

    for i in range(N):
        sn[0][i] = i + 1

    c, r, i = 0, N - 1, N + 1
    N -= 1
    while N != 0:
        for k in range(4):
            for _ in range(1, N+1):
                c += di[k]
                r += dj[k]
                sn[c][r] = i
                i += 1
            if (k == 1) or (k == 3):
                N -= 1
            if N == 0:
                break
    for s in sn:
        print(*s)
