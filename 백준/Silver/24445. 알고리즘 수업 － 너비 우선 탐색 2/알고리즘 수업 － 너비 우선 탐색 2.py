import sys
from collections import deque
input = sys.stdin.readline


def bfs(st_node):
    global j
    Q = deque([st_node])
    visited[st_node] = j

    while Q:
        curr = Q.popleft()
        for adj in adj_lst[curr]:
            if not visited[adj]:
                j += 1
                visited[adj] = j
                Q.append(adj)


N, M, R = map(int, input().split())
adj_lst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

for i in adj_lst:
    i.sort(reverse=True)

j = 1
bfs(R)
for i in range(1, N + 1):
    print(visited[i])