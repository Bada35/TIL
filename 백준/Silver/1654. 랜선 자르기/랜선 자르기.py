import sys
input = sys.stdin.readline


def binary_search(left, right):
    if left > right:
        return right

    mid = (left + right) // 2

    if line_cnt(mid) >= N:
        return binary_search(mid + 1, right)
    else:
        return binary_search(left, mid - 1)


def line_cnt(length):
    cnt = 0
    if not length:
        length = 1
    for l in line:
        cnt += l // length
    return cnt


K, N = map(int, input().split())
line = []

for _ in range(K):
    line.append(int(input()))

max_len = sum(line) // N
min_len = min(line) // ((N // 3) + 1)

print(binary_search(min_len, max_len))
