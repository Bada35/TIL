def check(st, ed, res):
    global min_en

    res += en[st][ed]
    visited[ed] = True

    if all(visited):
        res += en[ed][0]
        min_en = min(min_en, res)
    else:
        for i in range(1, N):
            if not visited[i]:
                check(ed, i, res)

    visited[ed] = False
    res -= en[st][ed]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    en = [list(map(int, input().split())) for _ in range(N)]  # en[x][y] : x출발 y도착 energy
    min_en = float('inf')

    for i in range(1, N):  # i:첨에 가는곳
        visited = [True] + [False] * (N - 1)
        check(0, i, 0)

    print(f'#{tc} {min_en}')
