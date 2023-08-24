T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # Map의 크기
    village = [list(map(int, input().split())) for _ in range(N + 1)]
    house = []  # 집 위치 좌표 튜플
    distance = []  # 거리 append

    for r in range(N + 1):
        for c in range(N + 1):
            if not village[r][c]:
                continue
            elif village[r][c] == 1:
                house.append((r, c))
            else:
                router = (r, c)

    for x, y in house:
        dist = ((x - router[0])**2 + (y - router[1])**2)**0.5
        distance.append(dist)

    res = max(distance)
    if res > int(res):
        res += 1

    print(f'#{tc} {int(res)}')





'''
최적화코드
1. 집의 위치(house)와 중계기의 위치(router)를 찾는 데에 두 번의 반복문을 돌 필요가 없습니다.
마을을 순회하며 중계기의 위치와 집의 위치를 동시에 찾을 수 있습니다.

2.최대 거리(res)를 찾을 때마다 모든 거리를 리스트에 저장할 필요가 없습니다.
집을 방문할 때마다 그 집과 중계기 사이의 거리를 계산하고, 그 거리가 현재까지의 최대 거리보다 큰 경우만 최대 거리를 업데이트 할 수 있습니다.

3.거리를 계산할 때 제곱근을 구할 필요가 없습니다.
거리의 제곱만 비교해도 됩니다. 제곱근을 구하는 연산은 비용이 크기 때문에 제외하는 것이 효율적입니다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N + 1)]

    house = []
    max_square_distance = 0

    for r in range(N + 1):
        for c in range(N + 1):
            if village[r][c] == 1:
                house.append((r, c))
            elif village[r][c] == 2:
                router = (r, c)

    for x, y in house:
        square_dist = (x - router[0])**2 + (y - router[1])**2
        if square_dist > max_square_distance:
            max_square_distance = square_dist

    res = max_square_distance**0.5
    if res > int(res):
        res += 1

    print(f'#{tc} {int(res)}')
'''
