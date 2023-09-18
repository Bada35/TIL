def binary_search(li, n):
    global cnt
    left = 0
    right = len(li) - 1
    curr = 0  # 번갈아중인지 확인 1:왼 2:오

    while left <= right:
        mid = (left + right) // 2
        if li[mid] == n:  # 번갈아와서 찾으면 cnt + 1
            cnt += 1
            break
        elif li[mid] < n:  # 왼쪽범위 선택하는 경우
            if curr == 1:
                break
            left = mid + 1
            curr = 1
        else:  # 오른쪽범위 선택하는경우
            if curr == 2:
                break
            right = mid - 1
            curr = 2


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    cnt = 0

    for b in B:
        binary_search(A, b)
    print(A, B)

    print(f'#{tc} {cnt}')


