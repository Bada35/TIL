# arr = [3,6,7,1,5,4]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()

# def subset_sum_count(N, K):
#     dp = [[0] * (K + 1) for _ in range(N + 1)]
#     dp[0][0] = 1  # 합이 0인 경우는 빈 집합 1개로 초기화
#
#     for i in range(1, N + 1):
#         for j in range(K + 1):
#             dp[i][j] = dp[i - 1][j]
#             if j >= i:
#                 dp[i][j] += dp[i - 1][j - i]
#
#     return dp[N][K]
#
# # 입력 받기
# N = 3
# K = 5
#
# # 부분집합 출력
def generate_subsets(idx, subset):
    if len(subset) == 3:
        print(subset)
        return

    if idx == 12:
        return

    generate_subsets(idx + 1, subset + [A[idx]])
    generate_subsets(idx + 1, subset)


for tc in range(1, T + 1):
    N, K = map(int, input().split())

    generate_subsets(0, [])

