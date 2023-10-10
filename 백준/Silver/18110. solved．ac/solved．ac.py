from sys import stdin
input = stdin.readline

n = int(input())
if not n:
    print(0)
    exit(0)
dif = [int(input()) for _ in range(n)]
dif.sort()
p_remove = int(n * 0.15 + 0.5)
print(int((sum(dif[p_remove:n - p_remove]) / (n - p_remove * 2)) + 0.5))
