input()
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    v = True
    if num == 1:
        continue
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            v = False
            break
    if v:
        cnt += 1

print(cnt)