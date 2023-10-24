for tc in range(1, int(input()) + 1):
    R, S = input().split()
    for s in S:
        print(s * int(R), end='')
    print()