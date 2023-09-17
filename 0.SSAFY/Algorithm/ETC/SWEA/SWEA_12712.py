# #     →  ↓  ←   ↑
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# #    ↘   ↙  ↖   ↖
# dk = [1, 1, 1, -1]
# dl = [1, -1, -1, -1]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     flies = [list(map(int, input().split())) for _ in range(N)]
#     max_flies = 0
#
#     for c in range(N):
#         for r in range(N):
#
#
#
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(M):  # i행 j열 원소에 대해(행 우선 순회)
            s = arr[i][j]
            for k in range(4):
                for p in range(1, arr[i][j] + 1):  # 풍선이 터진만큼 움직이기때문
                    ni, nj = i + di[k]*p, j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:  # 인덱스 범위 지정
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f"#{tc} {max_v}")