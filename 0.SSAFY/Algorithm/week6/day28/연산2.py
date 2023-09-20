def cal(num, target):
    global max_cnt

    visited = set()  # in 찾을때 list는 O(N) set는 변경하면 O(1) (by GPT)
    queue1 = [(num, 0)]  # (현재 숫자, 이 숫자까지의 cnt)
    queue2 = []  # 스택 2개로 큐 구현

    while queue1 or queue2:
        plus_cnt = 0

        if not queue2:
            while queue1:
                queue2.append(queue1.pop())

        curr_num, cnt = queue2.pop()

        if plus_cnt > 10 or curr_num > target + 20:
            continue

        if curr_num == target:  # target 찾으면 max_cnt 업데이트
            max_cnt = min(max_cnt, cnt)
            return

        if curr_num in visited:  # 이미 해봤던숫자
            continue

        visited.add(curr_num)

        for next_num in [curr_num + 1, curr_num - 1, curr_num - 10, curr_num * 2]:
            if next_num not in visited and 0 < next_num <= 1_000_000:
                if next_num - curr_num == 1:
                    plus_cnt += 1
                queue1.append((next_num, cnt + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다

    max_cnt = float('inf')
    cal(N, M)

    print(f'#{tc} {max_cnt}')