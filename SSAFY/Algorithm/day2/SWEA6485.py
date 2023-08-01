T = int(input())

for tc in range(1, T + 1):
    result = []
    N = int(input())
    A, B = zip(*(map(int, input().split()) for _ in range(N)))
    A, B = list(A), list(B)  # 튜플을 리스트로 변환
    P = int(input())
    C = [int(input()) for _ in range(P)]

    for stop_num in C:
        cnt = 0
        for i in range(N):
            if A[i] <= stop_num <= B[i]:
                cnt += 1
        result.append(cnt)

    print(f'#{tc}',*result)
#

# 현중님 코드
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     A = []
#     B = []
#     for i in range(N):
#         lst = list(map(int, input().split()))
#         A.append(lst[0])
#         B.append(lst[1])
#     P = int(input())
#     sol = ''
#     for i in range(P):
#         num = (int(input()))
#         cnt = 0
#         for j in range(N):
#             if A[j] <= num and num <= B[j]: cnt += 1
#         sol += str(cnt) + ' '
#
#     print(f'#{test_case}', sol)