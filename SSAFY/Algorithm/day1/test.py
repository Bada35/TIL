def find_difference(lst):
    min_num = lst[0]
    max_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return max_num - min_num


T = int(input())

for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print(f'#{i+1} {find_difference(a)}')
