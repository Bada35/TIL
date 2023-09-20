def find_(u, parent):
    if parent[u] == u:
        return u
    parent[u] = find_(parent[u], parent)
    return parent[u]


def union(u, v, parent, rank):
    u = find_(u, parent)
    v = find_(v, parent)
    if u == v:
        return

    if rank[u] > rank[v]:
        u, v = v, u

    parent[u] = v
    if rank[u] == rank[v]:
        rank[v] += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # N:노드수 M:간선수
    tmp_lst = list(map(int, input().split()))
    adj_lst = [[] for _ in range(N + 1)]  # 0-based로 인접리스트

    for i in range(0, M * 2, 2):
        adj_lst[tmp_lst[i]].append(tmp_lst[i + 1])
        adj_lst[tmp_lst[i+1]].append(tmp_lst[i])

    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for u, neighbors in enumerate(adj_lst):
        for v in neighbors:
            union(u, v, parent, rank)

    group_set = set()
    for i in range(N + 1):
        group_set.add(find_(i, parent))

    print(f'#{tc} {len(group_set) - 1}')  # 0-based라 0도 찝힘