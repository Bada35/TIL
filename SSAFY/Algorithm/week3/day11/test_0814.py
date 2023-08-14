def cal(a, b, c):
    return b + c if a == '+' else (b - c if a == '-' else (b * c if a == '*' else b / c))


T = int(input())

for tc in range(1, T + 1):
    s = input().split()
    st = []
    print(f'#{tc}', end=' ')
    for i in range(len(s) - 1):
        if s[i] not in '+-*/':
            st.append(s[i])
        else:
            if len(st) >= 2:
                j = int(st.pop())
                k = int(st.pop())
                st.append(cal(s[i], j, k))
            else:
                st.append('error')
                break

    print(f'#{tc} {st[-1]}')