from collections import deque


def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = True
    max_dep = -1
    res = []

    while Q:
        nd, dep = Q.popleft()
        if dep > max_dep:
            max_dep = dep
            res = [nd]
        elif dep == max_dep:
            res.append(nd)

        for adj in adj_lst[nd]:
            if not visited[adj]:
                visited[adj] = True
                Q.append((adj, dep + 1))

    return max(res)


for tc in range(1, 2):
    L, ST = map(int, input().split())
    a = list(map(int, input().split()))

    adj_lst = [[0] * 20 for _ in range(20)]
    for u, v in zip(a[::2], a[1::2]):
        adj_lst[u][v] = 1
    visited = [False] * 101
    for i in adj_lst:
        print(i)

    print(f'#{tc} {bfs(ST)}')


