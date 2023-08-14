di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(x, y):
    pass


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):  # 시작 x y 설정
        if miro[i].count('2') == 1:
            st_x = i
            st_y = miro[i].index('2')

    print(f'#{tc} {dfs(st_x, st_y)}')
