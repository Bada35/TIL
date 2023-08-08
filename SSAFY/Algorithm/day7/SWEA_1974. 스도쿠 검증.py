T = int(input())

for tc in range(1, T + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    li_2 = [[li[j][i] for j in range(9)] for i in range(9)]
    li_3 = [[li[i + k][j + l] for l in range(3) for k in range(3)] for i in (0, 3, 6) for j in (0, 3, 6)]
    li += li_2 + li_3
    cnt = 1
    for i in li:
        if len(set(i)) != 9:
            cnt = 0
            break
    print(f'#{tc} {cnt}')
