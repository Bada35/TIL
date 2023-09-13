# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로, memo[1]은 1로 초기화

# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
# n = 10  # 예시로 n을 10으로 가정
# memo = [0] * (n + 1)
# memo[0] = 0
# memo[1] = 1
#
# # 피보나치 수열의 처음 10개 항 출력
# for i in range(n + 1):
#     print(f"F({i}) = {fibo1(i)}")


# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
# memo = [0] * (n + 1)
# memo[0] = 0
# memo[1] = 1
# N = 10
# A = [0] * (N+1)
#
# A[0] = 0
# A[1] = 1
# A[2] = 1
#
# for i in range(3, N+1):
#     A[i] = A[i-1] + A[i-2]
#
# print(*A)

def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo1(n-1) + fibo1(n-2))
    return memo[n]

n = 10  # 예시로 n을 10으로 가정
memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1

# 피보나치 수열의 처음 10개 항 출력
for i in range(n + 1):
    print(f"F({i}) = {fibo1(i)}")