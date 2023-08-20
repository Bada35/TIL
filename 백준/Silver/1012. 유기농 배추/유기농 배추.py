# 인접 리스트 생성

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):

    baechu[x][y] = 0

    for d in range(4):
        ni, nj = x + di[d], y + dj[d]
        if 0 <= ni < N and 0 <= nj < M and baechu[ni][nj]:
            dfs(ni, nj)

    return 0


# 우 하 왼 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로 N: 세로 K: 배추 개수
    baechu = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        baechu[x][y] = 1

    cnt = 0
    for x in range(N):
        for y in range(M):
            if baechu[x][y]:
                dfs(x, y)
                cnt += 1

    print(cnt)

