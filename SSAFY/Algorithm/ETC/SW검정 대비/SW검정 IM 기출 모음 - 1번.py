# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    vi = [list(map(int, input().split())) for _ in range(N)]

    max_vi = 0

    for c in range(N):
        for r in range(N):
            virus = vi[c][r]
            res = vi[c][r]
            for i in range(1, P + 1):
                for d in range(4):
                    ni, nj = c + di[d]*i, r + dj[d]*i
                    if 0 <= ni < N and 0 <= nj < N:
                        res += vi[ni][nj]
            max_vi = max(max_vi, res)

    print(f'#{tc} {max_vi}')
