from sys import stdin
from collections import deque
input = stdin.readline


def stack(li):
    if li[0] == 'push':
        st.append(li[1])
    elif li[0] == 'front':
        if st:
            print(st[0])
        else:
            print(-1)
    elif li[0] == 'size':
        print(len(st))
    elif li[0] == 'empty':
        if not st:
            print(1)
        else:
            print(0)
    elif li[0] == 'pop':
        if not st:
            print(-1)
        else:
            print(st.popleft())
    else:
        if st:
            print(st[-1])
        else:
            print(-1)


st = deque()

for _ in range(int(input())):
    stack(list(input().split()))