T = int(input())
for tc in range(1, T + 1):
    t, n = map(str, input().split())
    print(t)
    nums = list(map(str, input().split()))

    GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    G_N = [0] * 10

    for num in nums:
        G_N[GNS.index(num)] += 1

    for i in range(10):
        for _ in range(G_N[i]):
            print(GNS[i], end=' ')
    print()