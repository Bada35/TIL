di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(x, y):
    if miro[x][y] == '3':
        return 1

    miro[x][y] = '1'  # 여기 왔다갔다고 표시

    for d in range(4):
        ni, nj = x + di[d], y + dj[d]
        if 0 <= ni < N and 0 <= nj < N and miro[ni][nj] != '1':
            if dfs(ni, nj):
                return 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):  # 미로 시작위치(2)의 x, y좌표 알아내기
        if miro[i].count('2') == 1:
            st_x = i
            st_y = miro[i].index('2')

    print(f'#{tc} {dfs(st_x, st_y)}')

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# def dfs(x, y):
#     pass
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     miro = [list(input()) for _ in range(N)]
#
#     for i in range(N):  # 시작 x y 설정
#         if miro[i].count('2') == 1:
#             st_x = i
#             st_y = miro[i].index('2')
#
#     print(f'#{tc} {dfs(st_x, st_y)}')
