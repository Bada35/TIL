T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sc = list(map(int, input().split()))

    cnt = 0
    for n in range(1, N + 1):  # 튕기는 거리 n : 1~N
        i = 0  # 탁자 번호 시작으로 초기화
        while i < N:  # 종료조건 : 튕겨나간 거리가 탁자보다 커지면
            cnt += sc[i]
            i += n  # 튕긴 후 다음 위치

    if cnt <= 0:  # 0점 이하인 경우 0점 출력
        cnt = 0

    print(f'#{tc} {cnt}')
