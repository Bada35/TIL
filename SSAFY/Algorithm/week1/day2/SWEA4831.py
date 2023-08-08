T = int(input())

for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = set(map(int, input().split()))

    now = 0
    cnt = 0
    next_station = now + K

    while next_station < N:
        if next_station in stations:
            cnt += 1
            now = next_station
        else:
            next_station -= 1

        if now + K == next_station:
            cnt = 0
            break

        next_station = now + K

    print(f'#{t} {cnt}')
