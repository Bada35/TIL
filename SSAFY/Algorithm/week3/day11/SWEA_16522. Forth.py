def cal(a, b, c):  # + - * / 계산
    return b + c if a == '+' else (b - c if a == '-' else (b * c if a == '*' else b // c))


T = int(input())

for tc in range(1, T + 1):
    s = input().split()
    st = []
    result = 'error'

    for i in range(len(s) - 1):
        if s[i] not in '+-*/':
            st.append(s[i])
        else:
            if len(st) >= 2:
                j = int(st.pop())
                k = int(st.pop())
                if j == 0:
                    continue
                st.append(cal(s[i], k, j))
            else:
                st.clear()
                break

    if len(st) == 1:
        result = st[-1]

    print(f'#{tc} {result}')