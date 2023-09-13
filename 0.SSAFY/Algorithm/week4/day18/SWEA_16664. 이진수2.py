def de2bi(n):
    res = []
    cnt = 0
    while n:
        if cnt > 12:
            return 'overflow'
        n *= 2
        tmp = int(n)
        res.append(tmp)
        n -= tmp
        cnt += 1
    return res


T = int(input())

for tc in range(1, T + 1):
    num = float(input())
    print(f'#{tc} {"".join(map(str, de2bi(num)))}')
