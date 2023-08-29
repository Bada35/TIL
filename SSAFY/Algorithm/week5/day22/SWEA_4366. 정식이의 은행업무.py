def bi_wrong(b):
    lst = []
    for i in range(len(b)):
        tmp = b[:]
        if b[i] == '1':
            tmp[i] = '0'
        else:
            tmp[i] = '1'
        lst.append(int(''.join(tmp), 2))
    return lst


def tri_wrong(t):
    for i in range(len(t)):
        tmp = t[:]
        for j in range(3):
            if tmp[i] != j:
                tmp[i] = str(j)
                n = int(''.join(tmp), 3)
                if n in bi_num:
                    return n


T = int(input())

for tc in range(1, T + 1):
    bi = list(input())
    tri = list(input())

    bi_num = bi_wrong(bi)
    print(f'#{tc} {tri_wrong(tri)}')
