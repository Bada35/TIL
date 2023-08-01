def min_charging_count(K, N, M, stations):
    current_pos = 0
    remaining_energy = K
    charging_count = 0

    for i in range(M):
        distance_to_next_station = stations[i] - current_pos

        if distance_to_next_station > remaining_energy:
            # 다음 충전소까지 갈 수 없으면 현재 위치의 충전소로 돌아가야 함
            current_pos = stations[i - 1]
            remaining_energy = K
            charging_count += 1

        remaining_energy -= distance_to_next_station
        current_pos = stations[i]

    # 마지막 충전소부터 종점까지의 거리를 계산하여 종점까지 갈 수 없는 경우 처리
    if N - current_pos > remaining_energy:
        charging_count += 1

    return charging_count


T = int(input())  # 테스트 케이스 개수
for t in range(1, T + 1):
    K, N, M = map(int, input().split())  # K: 최대 이동 가능 거리, N: 종점 위치, M: 충전소 개수
    stations = list(map(int, input().split()))  # 충전소 위치 정보
    result = min_charging_count(K, N, M, stations)
    print(f"#{t} {result}")
