import heapq

'''
다익스트라
1. 거리 배열(distance)을 생성하고, 시작 노드의 거리는 0으로, 다른 모든 노드의 거리는 무한대로 초기화
2. 방문하지 않은 노드 중에서 거리가 가장 작은 노드 선택
3. 선택한 노드를 '방문' 처리하고, 해당 노드의 이웃 노드들의 거리를 갱신
4. 모든 정점을 방문하면 알고리즘 종료
'''


def dijkstra(start):
    distance = {node: float('inf') for node in adj_lst}
    distance[start] = 0
    Q = [(0, start)]

    while Q:
        curr_dist, curr_node = heapq.heappop(Q)

        if curr_dist > distance[curr_node]:
            continue

        for n, w in adj_lst[curr_node].items():
            dist = curr_dist + w

            if dist < distance[n]:
                distance[n] = dist
                heapq.heappush(Q, (dist, n))

    return distance


for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())  # N:노드개수 E:간선수(도로개수)
    adj_lst = {i : {} for i in range(N + 1)}

    for _ in range(E):
        u, v, w = map(int, input().split())  # u:시작 v:도착 w:가중치
        adj_lst[u][v] = w

    print(adj_lst)

    dists = dijkstra(0)
    print(f'#{tc} {dists[N]}')