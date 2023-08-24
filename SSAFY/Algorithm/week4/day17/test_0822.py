import sys
input = sys.stdin.readline

N = int(input())  # 색종이의 개수
paper_area = [[0 for _ in range(1001)] for _ in range(1001)]
res = [0] * (N + 1)  # 각 색종이가 보이는 넓이 저장

for n in range(1, N + 1):
    x, y, width, height = map(int, input().split())

    # 해당 영역에 색종이 번호로 값을 업데이트
    for i in range(x, x + width):
        for j in range(y, y + height):
            paper_area[i][j] = n

# 각 색종이의 번호가 몇 번 등장하는지 카운트하여 넓이 계산
for i in range(1001):
    for j in range(1001):
        res[paper_area[i][j]] += 1

# 출력
for i in range(1, N + 1):
    print(res[i])
