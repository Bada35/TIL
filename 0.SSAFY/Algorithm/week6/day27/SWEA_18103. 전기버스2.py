def dfs(idx, charge):
    global min_cnt

    if idx in memo and memo[idx] <= charge:
        return

    # 메모
    memo[idx] = charge

    # 도착
    if idx == N - 1:
        min_cnt = min(min_cnt, charge)
        return

    for i in range(idx + 1, idx + bus_stops[idx] + 1):
        if i < N:
            dfs(i, charge + 1)


for tc in range(1, int(input()) + 1):
    bus_stops = list(map(int, input().split()))
    N = bus_stops.pop(0)
    min_cnt = float('inf')
    memo = {}
    dfs(0, 0)

    print(f'#{tc} {min_cnt - 1}')