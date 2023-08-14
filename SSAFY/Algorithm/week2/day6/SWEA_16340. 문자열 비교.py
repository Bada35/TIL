T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    str1 = str(input())
    str2 = str(input())
    try:
        if str2.index(str1):
            print(1)
    except ValueError:
        print(0)

# 영진 코드
# T = int(input())
# for tc in range(1, T + 1):
#     str1 = input()
#     str2 = input()
#     cnt = 0
#     if str1 in str2:
#         cnt += 1
#
#     print(f'#{tc} {cnt}')
