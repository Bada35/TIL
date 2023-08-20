from collections import deque


def bfs(st):
    Q = deque([st])
    visited = [False] * 101
    visited[st] = True

    while Q:
        node = Q.popleft()

        if node == 99:
            return 1

        for adj in adj_lst[node]:
            if not visited[adj]:
                visited[adj] = True
                Q.append(adj)

    return 0