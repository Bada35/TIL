T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            sum_pari = 0
            for i in range(M):
                for j in range(M):
                    sum_pari += flies[r + i][c + j]
            if sum_pari > max_sum:
                max_sum = sum_pari

    print(f'#{tc} {max_sum}')

# T = int(input())
#
#     for tc in range(1, T + 1):
#         N, M = map(int, input().split())
#         paris = [list(map(int, input().split())) for _ in range(N)]
#
#         max_pari = 0
#         for n in range(N - M + 1):
#             pari = 0
#             for m1 in range(M):
#                 for m2 in range(M):
#                     pari += paris[n + m1][n + m2]
#             if pari > max_pari:
#                 max_pari = pari
#
#         print(f'#{tc} {max_pari}')