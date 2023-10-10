from sys import stdin
input = stdin.readline


def stack(li):
    if li[0] == 'push':
        st.append(li[1])
    elif li[0] == 'top':
        if st:
            print(st[-1])
        else:
            print(-1)
    elif li[0] == 'size':
        print(len(st))
    elif li[0] == 'empty':
        if not st:
            print(1)
        else:
            print(0)
    else:
        if not st:
            print(-1)
        else:
            print(st.pop())


st = []

for _ in range(int(input())):
    stack(list(input().split()))