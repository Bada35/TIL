for tc in range(1, 11):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]
    dia = [0, 0]
    max_sum = 0

    for i in range(100): # 가로세로
        dia[0] += nums[i][i]
        dia[1] += nums[i][99-i]
        result = 0
        for j in range(100):
            result += nums[j][i]
        max_sum = max(max_sum, result, sum(nums[i]))

    max_sum = max(dia[0], dia[1], max_sum)
    print(f'#{tc} {max_sum}')