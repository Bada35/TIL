T = int(input())

for tc in range(1, T + 1):
    s = input()
    stack = []
    cnt = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack[-1] + 1 == i:
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1

    print(f'#{tc} {cnt}')
