from collections import deque

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(x, y):
    Q = deque([(x, y)])
    visited[x][y] = 1

    while Q:
        i, j = Q.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if miro[ni][nj] == '3':
                    return 1
                if miro[ni][nj] == '0' and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    Q.append((ni, nj))
    return 0


for tc in range(1, 11):
    input()
    miro = [list(input()) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]

    print(f'#{tc} {bfs(1, 1)}')
