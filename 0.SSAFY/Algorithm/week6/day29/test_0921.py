import heapq
import sys
input = sys.stdin.readline


def dijkstra(start, graph):
    dists = {node: float('inf') for node in graph}
    dists[start] = 0  # 1. 시작 노드의 거리는 0으로, 그 외의 노드들의 거리는 무한대로 설정
    Q = [(0, start)]

    while Q:
        curr_dist, curr_node = heapq.heappop(Q)

        if curr_dist > dists[curr_node]:
            continue

        for n, w in graph[curr_node].items():  # [(key1, value1), (key2, value2)] 형태로 반환
            dist = curr_dist + w

            if dist < dists[n]:
                dists[n] = dist
                heapq.heappush(Q, (dist, n))

    return dists


def init():
    v, e = map(int, input().split())
    st = int(input())
    graph = {i: {} for i in range(v + 1)}

    for _ in range(e):
        s, ed, w = map(int, input().split())
        if ed in graph[s]:
            graph[s][ed] = min(graph[s][ed], w)  # 여러 개 간선중 작은것만 저장
        else:
            graph[s][ed] = w

    return v, e, st, graph


V, E, ST, graph = init()
# print(V, E, ST, graph, sep='\n')

distances = dijkstra(ST, graph)

for i in range(1, V + 1):
    if distances.get(i) == float('inf'):
        print("INF")
    else:
        print(distances[i])
