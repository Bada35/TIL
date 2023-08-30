def cost(st, end, res):
    global min_cost, visited

    visited[end] = True
    res += li[st][end]

    if all(visited):
        res += li[end][0]
        min_cost = min(min_cost, res)
    else:
        for i in range(N):
            if not visited[i]:
                cost(end, i, res)

    visited[end] = False
    res -= li[st][end]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    # li[x][y] : x에서 y로 가는 비용
    min_cost = float('inf')

    for i in range(1, N):
        visited = [True] + [False] * (N - 1)
        cost(0, i, 0)

    print(f'#{tc} {min_cost}')
