import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(st_node):
    global j
    visited[st_node] = j
    j += 1
    for adj in adj_lst[st_node]:
        if not visited[adj]:
            dfs(adj)


N, M, R = map(int, input().split())
adj_lst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

for i in adj_lst:
    i.sort()

j = 1
dfs(R)
for i in range(1, N + 1):
    print(visited[i])
