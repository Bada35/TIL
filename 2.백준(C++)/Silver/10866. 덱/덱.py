from sys import stdin
from collections import deque
input = stdin.readline


def stack(li):
    if li[0] == 'push_front':
        st.appendleft(li[1])
    elif li[0] == 'push_back':
        st.append(li[1])
    elif li[0] == 'pop_front':
        print(st.popleft() if st else -1)
    elif li[0] == 'pop_back':
        print(st.pop() if st else -1)
    elif li[0] == 'size':
        print(len(st))
    elif li[0] == 'empty':
        print(0 if st else 1)
    elif li[0] == 'front':
        print(st[0] if st else -1)
    else:
        print(st[-1] if st else -1)


st = deque()

for _ in range(int(input())):
    stack(list(input().split()))