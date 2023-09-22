import heapq


def kruskal(adj_lst):
    parent = {i: i for i in adj_lst.keys()}
    edges = []
    for u, neighbors in adj_lst.items():
        for v, w in neighbors.items():
            edges.append((w, u, v))
    edges.sort()

    mst_weight = 0
    for w, u, v in edges:
        if find_(parent, u) != find_(parent, v):
            union(parent, u, v)
            mst_weight += w

    return mst_weight


def prim(adj_lst):
    mst_weight = 0
    visited = set()
    start_node = list(adj_lst.keys())[0]
    edges = [(0, start_node)]

    while edges:
        w, u = heapq.heappop(edges)
        if u not in visited:
            visited.add(u)
            mst_weight += w
            for v, w in adj_lst[u].items():
                if v not in visited:
                    heapq.heappush(edges, (w, v))

    return mst_weight


def find_(parent, u):
    if parent[u] == u:
        return u
    return find_(parent, parent[u])


def union(parent, u, v):
    u = find_(parent, u)
    v = find_(parent, v)
    if u != v:
        parent[v] = u


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj_lst = {i: {} for i in range(V + 1)}

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj_lst[u][v] = w
        adj_lst[v][u] = w

    # min_weight = kruskal(adj_lst)
    min_weight = prim(adj_lst)

    print(f'#{tc} {min_weight}')