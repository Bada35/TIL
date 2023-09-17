def cal(s):
    nums = [int(i) for i in s if i not in '+*']
    ops = [i for i in s if i in '+*']
    re = []
    for i in range(len(ops)):
        op = ops.pop()
        if op == '+':
            re.append(nums.pop())
        else:
            nums.append(nums.pop() * nums.pop())

    return sum(re + nums)


# def eva(lst):  # 재귀로 호출되면서, 더이상 ()가 중첩 안되어있을 경우 cal(lst)반환
#     if not lst.count('('):


for tc in range(1, 11):
    N = int(input())
    eq = list(input())
    st = []

    print(f'#{tc} {eq[1:N-1]}')
