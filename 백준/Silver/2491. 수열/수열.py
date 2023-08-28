N = int(input())
num = list(map(int, input().split()))

asc_cnt = 1
dsc_cnt = 1
max_cnt = []

for i in range(1, N):
    if num[i] > num[i - 1]:
        asc_cnt += 1
        max_cnt.append(dsc_cnt)
        dsc_cnt = 1
    elif num[i] < num[i - 1]:
        dsc_cnt += 1
        max_cnt.append(asc_cnt)
        asc_cnt = 1
    else:
        asc_cnt += 1
        dsc_cnt += 1
    # print(f'num:{num[i]} asc_cnt:{asc_cnt} dsc_cnt:{dsc_cnt}')

max_cnt.append(asc_cnt)
max_cnt.append(dsc_cnt)

print(max(max_cnt))
