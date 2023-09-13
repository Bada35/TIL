# def cnt_house(x, y, k):  # x,y:시작위치 k:범위
#     cnt = 0
#     for i in range(x - k + 1, x + k):
#         for j in range(y - abs(k - 1 - abs(i - x)), y + abs(k - 1 - abs(i - x)) + 1):
#             if 0 <= i < N and 0 <= j < N:
#                 cnt += city[i][j]
#     return cnt

arr = [[0] * 10 for _ in range(10)]
x = 2
y = 3
k = 3
print(f'range({x - k + 1}, {x + k})')
for i in range(0, 5):
    print(f'range({y - abs(k - 1 - abs(i - x))}, {y + abs(k - 1 - abs(i - x)) + 1})')

for i in range(x - k + 1, x + k):
    for j in range(y - abs(k - 1 - abs(i - x)), y + abs(k - 1 - abs(i - x)) + 1):
        arr[i][j] = 1

print(*arr, sep='\n')