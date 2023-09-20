def dfs(factory, product, curr_sum):
    global min_val

    visited[factory] = True
    curr_sum += values[product][factory]

    # 유망X
    if curr_sum >= min_val:
        return

    if all(visited):
        min_val = curr_sum  # 위에서 걸러서 비교할필요 x
        return

    for i in range(N):
        if not visited[i]:
            dfs(i, product + 1, curr_sum)
            visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    values = [list(map(int, input().split())) for _ in range(N)]
    min_val = sum([values[i][i] for i in range(N)])  # 대각선으로 min_val 설정(inf보다 초반에 더 잘 거르지않을까?)

    for i in range(N):
        visited = [False] * N
        dfs(i, 0, 0)

    print(f'#{tc} {min_val}')