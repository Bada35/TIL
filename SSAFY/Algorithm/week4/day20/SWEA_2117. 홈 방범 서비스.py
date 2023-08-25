price = [0] + [k * k + (k - 1) * (k - 1) for k in range(1, 22)]


def cnt_house(x, y, k):  # x,y:시작위치 k:범위
    cnt = 0
    for i in range(x - k + 1, x + k):
        for j in range(y - abs(k - 1 - abs(i - x)), y + abs(k - 1 - abs(i - x)) + 1):
            if 0 <= i < N and 0 <= j < N:
                cnt += city[i][j]
    return cnt


def service():
    max_house = 0
    for x in range(N):
        for y in range(N):
            for k in range(N+1, 0, -1):  # k:배율, 최대커버니까 찾으면 바로 break, (N,0,-1)하면 tc10에서 오류
                house = cnt_house(x, y, k)
                if price[k] <= house * M:
                    max_house = max(max_house, house)
                    break
    return max_house


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:도시의 크기 M:하나의 집이 지불할 수 있는 비용
    city = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {service()}')

