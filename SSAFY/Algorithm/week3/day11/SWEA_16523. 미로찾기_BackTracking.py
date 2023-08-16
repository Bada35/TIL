di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bt(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or miro[x][y] == '1':
        return 0

    if miro[x][y] == '3':
        return 1

    miro[x][y] = '1'

    for d in range(4):
        ni, nj = x + di[d], y + dj[d]
        if bt(ni, nj):
            return 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    for i in range(N):
        if miro[i].count('2') == 1:
            st_x = i
            st_y = miro[i].index('2')

    print(f'#{tc} {bt(st_x, st_y)}')