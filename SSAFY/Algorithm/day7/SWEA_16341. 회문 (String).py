# T = int(input())
# for tc in range(1, T + 1):
#     print(f'#{tc}', end=' ')
#     N, M = map(int, input().split())
#     li = [str(input()) for _ in range(N)]
#     li_2 = [''.join(row[i] for row in li) for i in range(len(li[0]))]
#     li += li_2
#     for j in range(N * 2):
#         for i in range(N - M + 1):  # 찾는 글자수에 따라 몇번 하는지
#             if li[j][i:i+(M//2)] == li[j][i+M-1:i+(M//2)-1+(M % 2):-1]:
#                 print(li[j][i:i+M])

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N, M = map(int, input().split())
    li = [input() for _ in range(N)]
    li += [''.join(row[i] for row in li) for i in range(len(li[0]))]
    for j in range(N * 2):
        for i in range(N - M + 1):
            if li[j][i:i+(M//2)] == li[j][i+M-1:i+(M//2)-1+(M % 2):-1]:
                print(li[j][i:i+M])