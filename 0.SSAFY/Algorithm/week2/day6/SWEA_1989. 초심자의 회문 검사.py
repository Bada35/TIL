T = int(input())
for tc in range(1, T + 1):
    st = str(input())
    re = 1
    for i in range(len(st) // 2):
        if st[i] != st[len(st) - 1 - i]:
            re = 0
            break
    print(f'#{tc} {re}')

