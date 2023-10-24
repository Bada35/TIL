def dfs(factory, product, curr_sum):
    global max_score

    visited[factory] = True
    curr_sum += scores[product][factory]

    # 유망X
    # if curr_sum <= max_val:
    #     return

    if all(visited):
        max_score = max(max_score,curr_sum)  # 위에서 걸러서 비교할필요 x
        return

    for i in range(N):
        if not visited[i]:
            dfs(i, product + 1, curr_sum)
            visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    max_score = float('-inf')

    for i in range(N):
        visited = [False] * N
        dfs(i, 0, 0)

    print(f'#{tc} {max_score}')
