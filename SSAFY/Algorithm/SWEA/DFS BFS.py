import sys
from collections import deque
input = sys.stdin.readline

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N or houses[x][y] == 0:
        return 0

    houses[x][y] = 0
    cnt += 1

    for d in range(4):
        ni, nj = x + di[d], y + dj[d]
        if dfs(ni, nj):
            return 1

    return 0  # 그 좌표에서 모든 탐색이 끝났을 경우 탈출 위해


def bfs(x, y):
    global cnt
    Q = deque([(x, y)])
    houses[x][y] = 0

    while Q:
        curr = Q.popleft()
        for d in range(4):
            ni, nj = curr[0] + di[d], curr[1] + dj[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N or houses[ni][nj] == 0:
                continue
            cnt += 1
            houses[ni][nj] = 0
            Q.append([ni, nj])

    return 0


N = int(input())
houses = [list(map(int, input().strip())) for _ in range(N)]
danji_cnt = 0
danji = []
cnt = 1

for c in range(N):
    for r in range(N):
        if houses[c][r]:  # 1 찾으면
            danji_cnt += 1
            bfs(c, r)
            danji.append(cnt)
            cnt = 1

print(danji_cnt, *sorted(danji), sep='\n')

