def min_processing_time(times):
    N = len(times)
    times.sort()  # Sort the list in ascending order

    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + times[i - 1]

    min_time = dp[N]
    for i in range(1, N):
        min_time += dp[i]

    return min_time

N = int(input())
times = list(map(int, input().split()))

result = min_processing_time(times)
print(result)
