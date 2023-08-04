T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    li = [0]*10

    for i in range(10):
        if (i % 2) == 0:
            k = arr.index(max(arr))
            li[i] = arr.pop(k)
        else:
            k = arr.index(min(arr))
            li[i] = arr.pop(k)

    print(f'#{tc}', *li)

