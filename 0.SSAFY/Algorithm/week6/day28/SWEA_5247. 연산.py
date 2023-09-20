
def cal(num, target, visited, cnt=0, plus_cnt=0):
    global min_cnt

    if plus_cnt > 10 or num > target + 20:
        return

    if num == target:  # target 찾으면 min_cnt 업데이트
        min_cnt = min(min_cnt, cnt)
        return

    if num in visited:  # 이미 해봤던숫자
        return

    visited.add(num)

    for next_num in [num + 1, num - 1, num - 10, num * 2]:
        if next_num not in visited and 0 < next_num <= 1_000_000:
            next_plus_cnt = plus_cnt + 1 if next_num - num == 1 else 0
            cal(next_num, target, visited, cnt + 1, next_plus_cnt)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다

    min_cnt = float('inf')
    visited = set()  # in 찾을때 list는 O(N) set는 변경하면 O(1) (by GPT)
    cal(N, M, visited)

    print(f'#{tc} {min_cnt}')