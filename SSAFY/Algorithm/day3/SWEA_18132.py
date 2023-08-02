T = int(input())


def subset_sum_count(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1  # 합이 0인 경우는 빈 집합 1개로 초기화

    for i in range(1, N + 1):
        for j in range(K + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= i:
                dp[i][j] += dp[i - 1][j - i]

    return dp[N][K]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(range(1, N + 1))
    print(f'#{tc} {subset_sum_count(N, K)}')
