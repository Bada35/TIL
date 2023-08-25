import sys
input = sys.stdin.readline


def vs(a, b):
    for card in ['4', '3', '2', '1']:
        if a.count(card) > b.count(card):
            return 'A'
        elif a.count(card) < b.count(card):
            return 'B'
    return 'D'


N = int(input())
for tc in range(1, N + 1):
    A = input().split()[1:]
    B = input().split()[1:]
    print(vs(A, B))
