def fact(n):
    return 1 if n == 0 else n * fact(n-1)

N, K = map(int, input().split())

print(fact(N) // (fact(K) * fact(N - K)))
