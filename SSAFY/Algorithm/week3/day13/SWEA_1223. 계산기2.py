for tc in range(1, 11):
    N = int(input())
    s = list(input())

    nums = [int(i) for i in s if i not in '+*']  # 숫자만 저장
    ops = [i for i in s if i in '+*']  # 연산자만 저장

    re = []
    for i in range(len(ops)):  # while ops
        op = ops.pop()  # 연산자에 대해
        if op == '+':  # + 면 result 리스트로 보내버리기
            re.append(nums.pop())
        else:  # * 면 곱한 후 원래 리스트에 넣어놓기
            nums.append(nums.pop() * nums.pop())

    # result 엔 +하면 될것들, nums엔 곱하기한 애들
    print(f'#{tc} {sum(re + nums)}')


'''    
정석풀이(시은)

def transform(before):
    priority = {'+': 1, '*': 2}
    after = ''
    stack = []
    for x in before:
        if x not in '+*':
            after += x
        else:
            if not stack:  # stack이 비어있으면,
                stack.append(x)
            else:
                if not stack or priority[x] > priority[stack[-1]]:
                    stack.append(x)
                elif priority[x] <= priority[stack[-1]]:
                    while stack and priority[x] <= priority[stack[-1]]:
                        after += stack.pop()
                    stack.append(x)
    while stack:
        after += stack.pop()
    return after


def calculate(formula):
    num_stack = []
    for x in formula:
        if x not in '+*':
            num_stack.append(int(x))
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            if x == '+':
                num_stack.append(b + a)
            elif x == '*':
                num_stack.append(b * a)
    # print(num_stack)
    return num_stack.pop()


for test in range(1, 11):
    N = int(input())
    before = input()
    after = transform(before)
    # print(after)
    result = calculate(after)
    print(f'#{test} {result}')'''
