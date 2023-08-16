# import sys
# input = sys.stdin.readline
#
# def dfs(node):
#     stack = [node]  # 노드 초기화
#     global i  # 방문 순서 저장용
#     st = []
#     visited[node] = True
#     while stack:
#         node = stack.pop()
#         st.append(node)
#         # result[node - 1] = i
#         # i += 1
#
#         for next_node in adj_lst[node]:
#             if not visited[next_node]:
#                 stack.append(next_node)
#                 visited[next_node] = True
#     for i in
#
#
# N, M, R = map(int, input().split())
# adj_lst = [[] for _ in range(N)]
# for _ in range(M):  # 인접리스트 생성
#     u, v = map(int, input().split())
#     adj_lst[u].append(v)
#     adj_lst[v].append(u)
# for i in adj_lst:
#     i.sort()
# print(adj_lst)
# result = [0] * N
# i = 1
# visited = [False] * (N + 1)
# dfs(R)
#
# for j in result:
#     print(j)