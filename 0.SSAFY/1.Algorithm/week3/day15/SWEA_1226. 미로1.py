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
            if 1 <= ni < 14 and 1 <= nj < 14:
                if miro[ni][nj] == '3':
                    return 1
                if miro[ni][nj] == '0' and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    Q.append((ni, nj))
    return 0


for tc in range(1, 11):
    input()
    miro = [list(input()) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    print(f'#{tc} {bfs(1, 1)}')
