for tc in range(1, int(input()) + 1):
    H, W, N = map(int, input().split())
    fl = N % H
    ho = (N // H) + 1

    if not N % H:
        fl = H
        ho -= 1

    print(f'{fl}{ho:02}', sep='')