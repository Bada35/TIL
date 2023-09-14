from collections import deque

N, K = map(int, input().split())
belts = deque(map(int, input().split()))

up_id = 0  # 올리는 위치
down_id = N  # 내리는 위치
break_cnt = 0  # 내구도 0인 개수
robots = deque([0]*N)  # 로봇들 현재 위치 (0: 로봇 없음, 1: 로봇 있음)
turn = 0  # 몇 번째 단계인지

while break_cnt < K:
    turn += 1

    # 1. 벨트와 로봇 이동
    belts.rotate(1)
    robots.rotate(1)
    robots[-1] = 0  # 로봇이 내리는 위치에 도착하면 로봇 내림

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i+1] and belts[i+1]:
            robots[i] = 0
            robots[i+1] = 1
            belts[i+1] -= 1
            if belts[i+1] == 0:
                break_cnt += 1

    robots[-1] = 0  # 로봇이 내리는 위치에 도착하면 로봇 내림

    # 3. 로봇 올리기
    if belts[0]:
        robots[0] = 1
        belts[0] -= 1
        if belts[0] == 0:
            break_cnt += 1

print(turn)
