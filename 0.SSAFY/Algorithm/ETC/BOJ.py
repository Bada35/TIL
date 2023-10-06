n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
a = [nums.count(i) for i in nums]
c = max(a)
b = []

for i in range(n):
    if a[i] == c:
        b.append(nums[i])

b = list(set(b))

if len(b) != 1:
    b = [b[1]]
print(int(round(sum(nums) / n)), nums[n // 2], b[0], max(nums) - min(nums), sep='\n')
