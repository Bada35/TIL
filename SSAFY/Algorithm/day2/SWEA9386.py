T = int(input())

def get_continuous_1(lst):
    max_num = 0
    count = 0
    for i in lst:
        if i == 1:
            count += 1
            if count > max_num:
                max_num = count
        else:
            count = 0
    return max_num

for tc in range(1, T + 1):
    N = int(input())
    input_string = input()
    numbers = list(map(int, input_string))
    print(f'#{tc} {get_continuous_1(numbers)}')



# YJ CODE
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = input()
#
#     cnt = 0
#     max_cnt = 0
#     for number in numbers:
#         if number == '1':
#             cnt += 1
#         else:
#             max_cnt = max(max_cnt, cnt)
#             cnt = 0
#     else:
#         max_cnt = max(max_cnt, cnt)
#
#     print(f'#{tc} {max_cnt}')
