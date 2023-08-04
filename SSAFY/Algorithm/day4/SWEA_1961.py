T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    li = [[''] * 3 for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for i in range(N - 1, -1, -1):
                if r == 0:
                    li[c][r] += arr[i][c]
                elif r < 3:
                    li[c][r] += li[i][r - 1][c]

    for i in range(N):
        for j in range(3):
            print(li[i][j], end=' ')
        print()
