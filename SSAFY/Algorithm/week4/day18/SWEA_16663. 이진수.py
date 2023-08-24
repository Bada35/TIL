for tc in range(1, int(input()) + 1):
    print(f'#{tc}', end=' ')
    n, n16 = input().split()

    for i in n16:
        print(format(int(i, 16), '04b'), end='')

    print()
