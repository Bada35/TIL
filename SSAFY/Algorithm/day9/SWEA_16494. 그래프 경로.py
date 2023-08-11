T = int(input())


def dfs(node):
    visited[node] = True
    for next_node in adj_lst[node]:
        if not visited[next_node]:
            dfs(next_node)


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]  # 인접lst
    visited = [False] * (V+1)
    for i in range(E):
        u, v = map(int, input().split())
        adj_lst[u].append(v)
    S, G = map(int, input().split())
    dfs(S)
    print(f'#{tc} {int(visited[G])}')
