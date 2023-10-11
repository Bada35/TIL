from sys import stdin
input = stdin.readline

res = -1
N = int(input())

for i in range(N // 5, -1, -1):
    if not (N - 5 * i) % 3:
        res = i + (N - 5 * i) // 3
        break
print(res)