def dfs(node):
    visited[node] = True
    for next_node in adj_lst[node]:
        if not visited[next_node]:
            dfs(next_node)


for tc in range(1, 11):
    t, E = map(int, input().split())
    adj_lst = [[] for _ in range(11)]
    visited = [False] * 11
    for i in range(E):
        u, v = map(int, input().split())
        adj_lst[u].append(v)
    print(adj_lst)
    S, G = map(int, input().split())
    dfs(S)
    print(f'#{tc} {int(visited[G])}')
