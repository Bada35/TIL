from collections import deque

N = int(input())
cards = deque([i for i in range(N, 0, -1)])

for _ in range(N - 1):
    cards.pop()
    cards.appendleft(cards.pop())

print(*cards)