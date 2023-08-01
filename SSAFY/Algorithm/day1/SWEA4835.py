T = int(input())

def get_difference(N, M, numbers):
    max_sum = min_sum = current_sum = sum(numbers[:M])

    for i in range(1, N - M + 1):
        current_sum = current_sum - numbers[i - 1] + numbers[i + M - 1]
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_sum)

    return max_sum - min_sum

for tc in range(T):
    nm = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    print(f'#{tc+1} {get_difference(nm[0], nm[1], numbers)}')