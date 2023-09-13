def service(st, ed, res):
    global min_dist

    res += dist[st][ed]
    visited[ed] = True

    if all(visited):
        res += to_home[ed]
        min_dist = min(min_dist, res)
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                service(ed, i, res)

    visited[ed] = False
    res -= dist[st][ed]


def cal_dist(i, j):
    return abs(coor[i] - coor[j]) + abs(coor[i + 1] - coor[j + 1])


T = int(input())

for tc in range(1, 2):
    N = int(input())
    coor = list(map(int, input().split()))
    to_home = []

    home_x = coor.pop(2)
    home_y = coor.pop(2)

    dist = [[] for _ in range(N + 1)]
    for i in range(0, 2 * (N + 1), 2):
        to_home.append(abs(home_x - coor[i]) + abs(home_y - coor[i + 1]))
        for j in range(0, 2 * (N + 1), 2):
            dist[i//2].append(cal_dist(i, j))

    visited = [False] * (N + 1)
    visited[0] = True
    min_dist = float('inf')

    for i in range(1, N + 1):
        service(0, i, 0)

    print(f'#{tc} {min_dist}')

