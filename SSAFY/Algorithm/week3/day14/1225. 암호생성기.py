def pw(n):
    while True:
        for i in range(1, 6):
            num = n.pop(0) - i
            if num <= 0:
                n.append(0)
                return n
            n.append(num)


for tc in range(1, 11):
    input()
    nums = list(map(int, input().split()))
    nums = [i - (min(nums)//15-1)*15 for i in nums]
    print(f'#{tc}', *pw(nums))
