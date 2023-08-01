T = int(input())

def get_difference(lst):
    max_num = lst[0]
    min_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    return max_num - min_num

for tc in range(1, T+1):
    N = int(input())
    pos_nums = list(map(int,input().split()))
    print(f'#{tc} {get_difference(pos_nums)}')