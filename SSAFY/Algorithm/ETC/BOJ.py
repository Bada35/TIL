import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N:전체날짜 K:연속날짜수
tmp = list(map(int, input().split()))
sum_tmp = sum(tmp[:K])
res = sum_tmp

for i in range(1, N - K + 1):
    sum_tmp = sum_tmp - tmp[i - 1] + tmp[i + K - 1]
    res = max(res, sum_tmp)

print(res)
