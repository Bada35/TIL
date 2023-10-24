from collections import deque


def dfs(node):
    print(node, end=' ')
    visited[node] = True

    for adj in adj_lst[node]:
        if not visited[adj]:
            dfs(adj)


def bfs(st_node):
    Q = deque([st_node])
    visited[st_node] = True

    while Q:
        node = Q.popleft()
        print(node, end=' ')

        for adj in adj_lst[node]:
            if not visited[adj]:
                visited[adj] = True
                Q.append(adj)


N, M, V = map(int, input().split())
adj_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)
for i in adj_lst:
    i.sort()
visited = [False] * (N + 1)
dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)
