# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    h = [list(map(int, input().split())) for _ in range(N)]
    bong = 0  # 봉우리 개수

    for c in range(N):
        for r in range(N):
            height = h[c][r]
            cnt = 1
            for k in range(4):  # 델타탐색
                i = c + di[k]
                j = r + dj[k]
                if 0 <= i < N and 0 <= j < N:  # 인덱싱에러
                    if h[i][j] >= height:  # 가운데보다 큰곳 있을경우 cnt = 0
                        cnt = 0
                        break
            bong += cnt

    print(f'#{tc} {bong}')
