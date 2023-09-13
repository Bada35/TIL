T = int(input())


def nol_e(n):
    dp = [0] * (n // 10)  # 50이 들어오면 0~5칸의 dp 생성
    dp[0] = 1
    for i in range(1, n//10):
        dp[i] = dp[i-1] * 2 + (-1)**(i + 1)
    return dp[n // 10 - 1]


for tc in range(1, T + 1):
    print(f'#{tc} {nol_e(int(input()))}')
