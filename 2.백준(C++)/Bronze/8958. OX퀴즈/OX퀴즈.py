import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    s = list(input())
    res = 0
    cnt = 1

    for i in s:
        if i == 'O':
            res += cnt
            cnt += 1
        else:
            cnt = 1

    print(res)