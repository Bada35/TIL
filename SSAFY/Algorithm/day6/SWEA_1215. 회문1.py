for tc in range(1, 11):
    s = int(input())
    li = [list(map(str, input())) for _ in range(8)]
    cnt = 0

    for i in range(8):  # 0~7행
        for j in range(8 - s + 1):  # 0~4 인덱스 열까지
            yn = 1
            for k in range(s // 2):  # 길이 // 2 번만
                if li[i][j + k] != li[i][j + s - k - 1]:
                    yn = 0
                    break
            if yn:
                cnt += 1

    for j in range(8):  # 0~7열
        for i in range(8 - s + 1):  # 0~4 인덱스 행까지
            yn = 1
            for k in range(s // 2):  # 길이 // 2 번만
                if li[i + k][j] != li[i + s - k - 1][j]:
                    yn = 0
                    break
            if yn:
                cnt += 1

    print(f'#{tc} {cnt}')

