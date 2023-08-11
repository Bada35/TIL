'''
7 7
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''


def dfs(node, visited):
    print(node)
    visited[node] = True

    for next_node in adj_list[node]:
        if not visited[next_node]:
            dfs(next_node, visited)


# n : node 수, m : 간선 수
n, m = map(int, input().split())

visited = [False] * (n + 1)
adj_list = [[] for _ in range(n+1)]
for i in range(n + 1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
print(adj_list)

dfs(1, visited)






# def fibo(n):
#     global cnt
#     global memo
#     cnt += 1
#     if n < 2:
#         return memo[n]
#     else:
#         if memo[n] == 0:
#             memo[n] = fibo(n-1) + fibo(n+2)


# def fibo(n):
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

# N = 30
# memo = [0]*(N+1)
# memo[0] = 0
# memo[1] = 1
# cnt = 0

# print(fibo(30))
