def paint_cnt(x, y):
    global min_cnt
    check_1 = 'WBWBWBWB'
    check_2 = 'BWBWBWBW'
    cnt_1 = 0
    cnt_2 = 0

    for i in range(8):
        if i % 2:
            for j in range(8):
                if boards[i + x][j + y] != check_1[j]:
                    cnt_1 += 1
                if boards[i + x][j + y] != check_2[j]:
                    cnt_2 += 1
        else:
            for j in range(8):
                if boards[i + x][j + y] != check_2[j]:
                    cnt_1 += 1
                if boards[i + x][j + y] != check_1[j]:
                    cnt_2 += 1

    min_cnt = min(min_cnt, cnt_1, cnt_2)


N, M = map(int, input().split())
boards = [list(input()) for _ in range(N)]
min_cnt = float('inf')

for x in range(N - 7):
    for y in range(M - 7):
        paint_cnt(x, y)

print(min_cnt)
