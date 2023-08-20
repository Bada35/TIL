T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    st_x, st_y, end_x, end_y = map(int, input().split())  # 시작x,y 좌표 / 끝 x,y 좌표
    area = [list(map(int, input().split())) for _ in range(N)]

    # 평균값 ev 구하기
    ev = 0
    for x in range(st_x, end_x + 1):
        for y in range(st_y, end_y + 1):
            ev += area[x][y]  # 평탄화 영역 총 합
    ev //= (end_y - st_y + 1) * (end_x - st_x + 1)  # ev = ev // (영역의 칸 수)

    # 작업 횟수 구하기
    cnt = 0
    for x in range(st_x, end_x + 1):
        for y in range(st_y, end_y + 1):
            if area[x][y] >= ev:  # 높이가 평균보다 크거나 같을 경우
                cnt += area[x][y] - ev
            else:  # 높이가 평균보다 작을 경우
                cnt += ev - area[x][y]

    print(f'#{tc} {cnt}')
