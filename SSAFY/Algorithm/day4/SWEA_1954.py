#    ↓   ←   ↑  →
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

for tc in range(1, 3):
    N = int(input())
    sn = [[0] * N for _ in range(N)]

    for i in range(N):
        sn[0][i] = i + 1

    print(sn)

    c, r, i = 0, N - 1, N + 1
    N -= 1
    while N != 0:
        for k in range(4):
            for p in range(N):
                c += di[k] * p
                r += dj[k] * p
                sn[c][r] = i
                i += 1
            if (k == 1) or (k == 3):
                N -= 1
            if N == 0:
                break

    print(sn)
