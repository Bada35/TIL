def bake(n, m, k, p):
    p.sort()

    for i in range(n):
        breads_made = (p[i] // m) * k
        breads_made -= i

        if breads_made <= 0:
            return "Impossible"
    return "Possible"


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    P = list(map(int, input().split()))
    print(f'#{tc} {bake(N, M, K, P)}')