from sys import stdin

while 1:
    li = list(map(int, stdin.readline().split()))
    if not li[0]:
        break
    li.sort()
    if li[0] ** 2 + li[1] ** 2 == li[2] ** 2:
        print('right')
    else:
        print('wrong')