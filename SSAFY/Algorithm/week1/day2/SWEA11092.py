T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {abs(len(numbers)-1-numbers[::-1].index(max(numbers))-numbers.index(min(numbers)))}')
