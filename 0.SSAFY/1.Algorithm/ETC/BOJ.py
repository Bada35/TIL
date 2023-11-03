import sys
input = sys.stdin.readline

N = int(input())
dol = list(map(int, input().split()))
max_cnt = float('-inf')

for j in range(N):
    cnt = 1
    max_num = dol[j]

    for i in dol[j:]:
        if i > max_num:
            max_num = i
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
