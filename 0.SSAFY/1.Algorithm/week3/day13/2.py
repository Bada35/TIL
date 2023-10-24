T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    routes = []
    student = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for _ in range(N):
        temp = student.pop()
        if temp[0] == temp[1]: # 들어가는 방 나가는 방 같으면 무시
            pass
        else:
            temp.sort()
            if temp[1] % 2 != 0:
                temp[1] += 1
            if temp[0] % 2 == 0:
                temp[0] -= 1
            routes.append(list(range(temp[0], temp[1]+1))) # 지나는 길을 숫자로 표현(방문 앞을 지난다고 생각하여 방번호 추가)

    while len(routes) != 0:
        occupied = routes[0] # 첫번째 학생이 지나간 길 추가
        next_route = []
        for i in range(1, len(routes)):
            intersection = set(occupied) & set(routes[i]) # i번째 학생과 이미 지나간 길이 겹쳤는지 확인
            if not intersection: # 지나간 적 없는 길이라면
                occupied.extend(routes[i]) # 이미 지나간 길에 추가
            else:
                next_route.append(routes[i])
        routes = next_route
        cnt += 1

    print(f'#{tc}', cnt)