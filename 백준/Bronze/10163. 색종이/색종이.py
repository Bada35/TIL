N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
areas = [0 for _ in range(N+1)]

for order in range(1, N+1):
    x, y, w, h = map(int, input().split())
    covered = 0
    for i in range(x, x+w):
        for j in range(y, y+h):
            if board[i][j] != 0:  # 이미 덮인 영역이라면
                areas[board[i][j]] -= 1  # 해당 영역의 색종이의 보이는 부분 넓이 감소
                covered += 1  # 겹친 영역 카운트 증가
            board[i][j] = order  # 보드 업데이트

    areas[order] = w*h - covered  # 현재 색종이의 보이는 부분 계산

for i in range(1, N+1):
    print(areas[i])
