import sys
input = sys.stdin.readline


def most_many(li, n):
    if len(li) == len(set(li)):
        if len(li) == 1:
            return li[0]
        return li[1]

    max_cnt = 1
    cnt = 0
    res = []

    for i in range(1, n):
        if li[i - 1] == li[i]:
            cnt += 1
        else:
            cnt = 0

        if cnt > max_cnt:
            res = [li[i]]
            max_cnt = cnt
        elif cnt == max_cnt:
            res.append(li[i])

    if len(res) == 1:
        return res[0]
    else:
        return res[1]


nums = []
n = int(input())

for tc in range(n):
    nums.append(int(input()))

nums.sort()

print(int(round(sum(nums) / n)))
print(nums[n//2])
print(most_many(nums, n))
print(nums[-1] - nums[0])
