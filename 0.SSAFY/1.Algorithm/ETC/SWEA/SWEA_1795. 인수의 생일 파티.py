for tc in range(1, int(input()) + 1):
    N, M, X = map(int, input().split())  # N:노드개수 M:간선수 X:인수집
    adj_list = {i: {} for i in range(N + 1)}  # 1-based라 +1
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj_list[x][y] = c
    # adj_list = {0: {}, 1: {2: 4, 3: 2, 4: 7}, 2: {1: 1, 3: 5}, 3: {1: 2, 4: 4}, 4: {2: 3}}
    