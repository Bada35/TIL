T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(input().split())
    for _ in range(M % N + 1):
        a = nums.pop(0)
        nums.append(a)
    print(f'#{tc} {nums[-1]}')