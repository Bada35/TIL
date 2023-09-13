for tc in range(1, 11):
    n = int(input())
    s = list(map(int, input().split('+')))

    print(f'#{tc} {sum(s)}')