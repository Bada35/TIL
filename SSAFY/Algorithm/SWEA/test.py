a = [2, 4, 7, 9, 11, 19, 23]


def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:  # 이진탐색의 종료조건 : 탐색 시작값이 탐색 종료값보다 커졌을 때
        mid = (start + end) // 2  # 중앙값
        if key < a[mid]:  # key 값이 중앙값보다 작은 경우
            end = mid - 1
        elif key > a[mid]:  # key 값이 중앙값보다 큰 경우
            start = mid + 1
        else:
            return True  # key 값과 중앙값이 같은 경우 : 검색 성공

    return False  # 검색 실패


print(binarySearch(a, len(a), 11))
print(binarySearch(a, len(a), 10))  # F
print(binarySearch(a, len(a), 2))
print(binarySearch(a, len(a), 4))
print(binarySearch(a, len(a), 7))
print(binarySearch(a, len(a), 9))
print(binarySearch(a, len(a), 19))
print(binarySearch(a, len(a), 23))
print(binarySearch(a, len(a), -1))  # F
print(binarySearch(a, len(a), 88))  # F
print(binarySearch(a, len(a), 0))  # F
print(binarySearch(a, len(a), 57))  # F
