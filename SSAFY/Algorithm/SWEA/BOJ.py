import sys
from collections import deque
input = sys.stdin.readline


def bfs(st_node):
    pass


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
bfs(R)
for i in range(1, N + 1):
    print(visited[i])