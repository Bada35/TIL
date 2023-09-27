import heapq

def daik():
    q = [(0,0)]

    while q:
        dist, now = heapq.heappop(q)


        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + next[0]
            distance[next[1]] = min(cost,distance[next[1]])
            heapq.heappush(q,(cost,next[1]))

T = int(input())
for test_case in range(1,T+1):
    N, E = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append((w,e))
    print(graph)
    distance = [int(1e9)] * (N+1)
    daik()
    print(f'#{test_case} {distance[N]}')