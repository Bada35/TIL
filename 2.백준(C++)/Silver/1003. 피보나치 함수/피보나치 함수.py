from sys import stdin
input = stdin.readline


memo = [[0, 0] for _ in range(41)]
memo[0], memo[1] = [1, 0], [0, 1]


def fib(n):
    if memo[n] != [0, 0]:
        return memo[n]

    memo[n-1] = fib(n-1)
    memo[n-2] = fib(n-2)

    memo[n] = [memo[n-1][0] + memo[n-2][0], memo[n-1][1] + memo[n-2][1]]

    return memo[n]


for tc in range(int(input())):
    num = int(input())
    print(*fib(num))