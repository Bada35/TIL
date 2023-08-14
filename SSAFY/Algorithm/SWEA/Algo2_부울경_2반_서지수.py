def gumsa(lst):  # 괄호검사
    st = []
    a = [c for c in lst if c in '(){}']
    for i in range(len(a)):
        if a[i] in '({':
            st.append(a[i])
        elif st[-1] + a[i] == '()' or st[-1] + a[i] == '{}':
            st.pop()
    if len(st):  # 스택에 뭐라도 남아있으면
        return -1
    else:
        return 1




T = int(input())
for tc in range(1, T + 1):
    s = list(input())
    stack = []  # 괄호용 스택
    num_stack = []  # 숫자용 스택
    result = 0

    if s[0] not in '(){}' or s[-1] not in '(){}' or gumsa(s) == -1:  # 숫자가 안 씌어지거나, 괄호검사 틀린경우
        result = -1
    # else:
    #     while 1:
    #         for i in range(len(s)):
    #             if s[i] in '{(':
    #                 stack.append(s[i])
    #                 num_stack.clear()
    #             elif s[i] not in ')}':
    #                 num_stack.append(int(s[i]))
    #             elif s[i] == ')':  # numstack에 있는애들 더하기
    #                 stack.pop()
    #                 sum_num = 0
    #                 for j in num_stack:
    #                     sum_num += j
    #                 num_stack.clear()
    #                 num_stack.append(sum_num)
    #             elif s[i] == '}':  # numstack에 있는애들 곱하기
    #                 stack.pop()
    #                 gop_num = 0
    #                 for j in num_stack:
    #                     gop_num += j
    #                 num_stack.clear()
    #                 num_stack.append(gop_num)



    print(f'#{tc} {result}')



