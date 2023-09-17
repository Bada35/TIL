def compare(a, b):
    return 'A' if a < b else 'B' if b < a else 0


def binary_search(books, target):
    def search(left, right, t, count):
        if left > right:  # 이진탐색 종료조건(첫범위가 끝범위보다 커지면)
            return count

        mid = (left + right) // 2  # 중간값
        count += 1  # 이진탐색 시작했으니 횟수 추가

        if t == mid:  # 중간값이랑 target이랑 같으면 종료
            return count
        elif t < mid:  # target값이 중간값보다 작으면 (왼쪽끝범위, 중간값-1)에서 탐색 실행
            return search(left, mid, t, count)
        else:  # target값이 중간값보다 크면 (중간값+1, 오른쪽끝범위)에서 탐색 실행
            return search(mid, right, t, count)

    return search(1, books, target, 0) #


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    print(f'#{tc} {compare(binary_search(P, A), binary_search(P, B))}')
