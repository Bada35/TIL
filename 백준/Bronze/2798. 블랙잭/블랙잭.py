from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

dif = float('inf')

for subsut in combinations(cards, 3):
    tmp = sum(subsut)
    if dif > M - tmp > 0:
        dif = M - tmp
        res = tmp
    if M - tmp == 0:
        print(tmp)
        exit(0)
print(res)
