T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzs = [list(map(int, input().split())) for _ in range(N)]
    suits = []

    for row in range(N):  # 열
        cnt = 0
        for col in range(N):  # 행
            if puzs[col][row] == 0:
                suits.append(cnt)
                cnt = 0
            else:
                cnt += 1
        suits.append(cnt)

    for col in range(N):  # 열
        cnt = 0
        for row in range(N):  # 행
            if puzs[col][row] == 0:
                suits.append(cnt)
                cnt = 0
            else:
                cnt += 1
        suits.append(cnt)

    print(f'#{tc} {suits.count(K)}')
