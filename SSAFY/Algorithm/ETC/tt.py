import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # 지금 있는 노드에서 인접 노드까지의 가중치?
    distances[start] = 0
    print(distances)
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        print(current_distance, current_node)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():  # [(key1, value1), (key2, value2)] 형태로 반환
            print(f'neighbor:{neighbor}, weight:{weight}')
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# 간단한 그래프 예시
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))