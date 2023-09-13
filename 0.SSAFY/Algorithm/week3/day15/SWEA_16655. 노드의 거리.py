from collections import deque


def bfs(s, g):
    Q = deque([(s, 0)])
    visited[s] = True

    while Q:
        n, res = Q.popleft()

        if n == g:
            return res

        for adj in adj_list[n]:
            if not visited[adj]:
                visited[adj] = True
                Q.append((adj, res + 1))

    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for i in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')

