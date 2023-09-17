for tc in range(10):
    N = int(input())
    lad = [list(map(int, input().split())) for _ in range(100)]

    nc = 99
    nr = lad[99].index(2)  # 현재 열 위치 lad[99][now]
    while nc != 0:
        if nr - 1 >= 0 and lad[nc][nr-1] == 1:  # 현재위치 왼쪽이 1이면
            while nr - 1 >= 0 and lad[nc-1][nr-1] == 0:  # 현재위치 왼쪽 위칸이 0인 동안
                nr -= 1
            nr -= 1
            nc -= 1
        elif nr + 1 < 100 and lad[nc][nr+1] == 1:  # 현재위치 오른쪽이 1이면
            while nr + 1 < 100 and lad[nc-1][nr+1] == 0:  # 현재위치 오른쪽 위칸이 0인 동안
                nr += 1  # 오른쪽 이동
            nr += 1
            nc -= 1
        else:
            nc -= 1
    print(f'#{tc} {nr}')
