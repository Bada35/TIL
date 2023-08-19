import sys
input = sys.stdin.readline


def dfs(st_node=1):
    global cnt
    visited[st_node] = True

    for adj in adj_lst[st_node]:
        if not visited[adj]:
            cnt += 1
            dfs(adj)
    return cnt


V = int(input())
E = int(input())
adj_lst = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
cnt = 0

for _ in range(E):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

print(dfs())

