def go_next(st_x, st_y, ed_x, ed_y):
    pass


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    apple_loca = [(0, 0)] + [0] * 11  # 사과 좌표, 0은 안쓸거고 최대 10개래서
    for y in range(N):
        for x in range(N):
            if maps[y][x]:
                apple_loca[maps[y][x]] = (x, y)

    res = 0
    for i in range(11):
        if not apple_loca[i]:
            break
        res += go_next(apple_loca[i][0], apple_loca[i][1], apple_loca[i+1][0], apple_loca[i+1][1])

    print(f'#{tc} {res}')


