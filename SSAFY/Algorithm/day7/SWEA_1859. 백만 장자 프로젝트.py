
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    buy = []
    result = 0

    while len(price) != 0:
        mx = max(price)
        mx_id = price.index(mx)
        for i in range(mx_id):
            buy.append(price[i])
        result += (mx * len(buy)) - sum(buy)
        buy.clear()
        price = price[mx_id+1:]

    print(f'#{tc} {result}')
