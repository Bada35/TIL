# T = int(input())
#
# for tc in range(1, T + 1):
#     col, row = map(int, input().split())
#     ballons = [list(map(int, input().split())) for _ in range(col)]
#     max_result = 0
#
#     for c in range(col): # 행
#         for r in range(row): # 열
#             result = 0
#             for i in range(c - ballons[c][r], c + ballons[c][r]+1):
#                 if 0 <= i < col:
#                     result += ballons[i][r]
#
#             for j in range(r - ballons[c][r], r + ballons[c][r]+1):
#                 if 0 <= j < row:
#                     result += ballons[c][j]
#
#             result -= ballons[c][r]
#             max_result = max(max_result, result)
#
#     print(f'#{tc} {max_result}')



di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                for p in range(1, arr[i][j] + 1):
                    ni, nj = i + di[k]*p, j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    print(f"#{tc} {max_v}")

