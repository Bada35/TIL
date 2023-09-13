def find(x, y, res):
    global min_sum

    res += li[x][y]

    if res > min_sum:
        return

    if (x, y) == (N - 1, N - 1):
        min_sum = min(min_sum, res)
        return

    for dx, dy in [(x + 1, y), (x, y + 1)]:
        if dx < N and dy < N:
            find(dx, dy, res)

    return min_sum


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    print(f'#{tc} {find(0, 0, 0)}')