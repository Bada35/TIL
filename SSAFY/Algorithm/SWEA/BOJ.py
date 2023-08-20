# from collections import deque
# import sys
# input = sys.stdin.readline
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
#
# def bfs():
#     Q = deque([(0, 0)])
#     cnt = 1
#
#     while Q:
#         curr_x, curr_y = Q.popleft()
#         miro[curr_x][curr_y] = 0
#         is_return = 1
#         for d in range(4):
#             ni, nj = curr_x + di[d], curr_y + dj[d]
#             if 0 <= ni < N and 0 <= nj < M and miro[ni][nj]:
#                 if ni == N - 1 and nj == M - 1:
#                     return cnt
#                 Q.append([ni, nj])
#                 is_return = 0
#                 cnt += 1
#         if is_return:
#             cnt -= 1



# def bfs():
#     Q = deque([(0, 0, 1)])  # (x, y, cnt) 형태로 저장. cnt는 해당 위치까지의 거리.
#     miro[0][0] = 0  # 시작 위치 방문 처리
#
#     while Q:
#         curr_x, curr_y, cnt = Q.popleft()
#
#         # 목표 위치 도달 여부 판단
#         if curr_x == N-1 and curr_y == M-1:
#             return cnt
#
#         for d in range(4):
#             ni, nj = curr_x + di[d], curr_y + dj[d]
#             if 0 <= ni < N and 0 <= nj < M and miro[ni][nj]:
#                 miro[ni][nj] = 0  # 방문 처리
#                 Q.append((ni, nj, cnt + 1))
#
#
# N, M = map(int, input().split())
# miro = [list(map(int, input().strip())) for _ in range(N)]
# print(bfs())