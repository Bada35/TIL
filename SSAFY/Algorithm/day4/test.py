# for j in range(m):
#     for i in range(n):
#         f(Array[i][j])  # 필요한 연산 수행
#
# for i in range(n):
#     for j in range(m):
#         f(Array[i][j])  # 필요한 연산 수행
#
#
# for i in range(n):
#     for j in range(m):
#         f(Array[i][j + (m-1-2*j) * (i%2)])
#
# # i : 행의 좌표, len(arr)
# # j : 열의 좌표, len(arr[0])
# arr = [[1,2,3].[4,5,6],[7,8,9]]
#
# for i in range(3):
#     for j in range(3):
#         if i < j :
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  # SWAP


# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)


# def print_subset(bit, arr, n):
#     for i in range(n):
#         if bit[i]:
#             print(arr[i], end=' ')
#     print()  # 개행 위해
#
#
# arr = [1, 2, 3, 4]
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit, arr, 4)


# arr = [3, 6, 9, 1, 5, 4]
# n = len(arr)  # 원소의 개수
#
# for i in range(1 << n):  # 1<<n = 2ⁿ 즉 부분 집합의 개수만큼
#     subset = []
#     for j in range(n):  # 원소의 수 만큼 비트를 비교함
#         if i & (1 << j):  # for i in range(n):\n if bit[i]: 과 같은역할
#             subset.append(arr[j])
#     print(subset)


# arr = [1, 2, 3, 7, 8, 11]
# n = len(arr)
#
# for i in range(1 << n):
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#     print(subset)


# def sequentialSearch(a, n, key):
#     i = 0
#     while i < n and a[i] != key:
#         i = i + 1
#     if i < n:
#         return i
#     else:
#         return -1


# #    ↓   ←   ↑  →
# di = [1, 0, -1, 0]
# dj = [0, -1, 0, 1]
#
#
# N = 3
# sn = [[0] * N for _ in range(N)]
#
# for i in range(N):
#     sn[0][i] = i + 1
#
# print(sn)
#
# c, r, i = 0, N - 1, N + 1
# N -= 1
# print(f'c:{c} r:{r} i:{i} N:{N}')
#
# while 1:
#     for k in range(4):
#         print(f'k:{k}')
#         for p in range(1, N+1):
#             c += di[k] * p
#             r += dj[k] * p
#             print(f'sn[{c}][{r}]')
#             sn[c][r] = i
#             print(f'sn[{c}][{r}] = {sn[c][r]}')
#             i += 1
#         if k == 1 or k == 3:
#             N -= 1
#         if N == 0:
#             break
#     break
#
# print(sn)

# st = '694855'
# print(list(st))
# print(*list(st), sep='')
#
# for i in range(3,0,-1):
#     print(i)

print((-1)%2)
