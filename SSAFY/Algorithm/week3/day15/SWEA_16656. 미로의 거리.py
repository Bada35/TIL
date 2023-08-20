from collections import deque

# 우 하 왼 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(x, y):
    Q = deque([(x, y, 0)])

    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    while Q:
        x, y, res = Q.popleft()

        if miro[x][y] == 3:
            return res - 1

        for d in range(4):
            ni, nj = x + di[d], y + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if miro[ni][nj] in [0, 3]:
                    visited[ni][nj] = True
                    Q.append((ni, nj, res + 1))

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        if miro[i].count(2) == 1:
            st_x = i
            st_y = miro[i].index(2)

    print(f'#{tc} {bfs(st_x, st_y)}')

