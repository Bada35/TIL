from sys import stdin
input = stdin.readline

N = int(input())
s = [0] * 10001

for _ in range(N):
    s[int(input())] += 1

cnt = 0
for i in range(1, 10001):
    for j in range(s[i]):
        print(i)
        cnt += 1
    if cnt == N:
        break
