di = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]  # 주변 좌표 12시부터 시계


def firstset(n, b):  # 초기세팅 Black:1 White:2
    b[n // 2][n // 2 + 1], b[n // 2 + 1][n // 2] = 1, 1
    b[n // 2][n // 2], b[n // 2 + 1][n // 2 + 1] = 2, 2


def place(x, y, c1):  # c1: 지금 놓는 color
    board[x][y] = c1
    c2 = 2 if c1 == 1 else 1  # c2 : 반대편돌 color

    for dx, dy in di:  # 방향탐색
        nx, ny = x + dx, y + dy
        dol = []

        # 인덱스에러 방어조건 + 반대편 돌인 동안
        while 0 < nx < len(board) and 0 < ny < len(board) and board[nx][ny] == c2:
            dol.append((nx, ny))
            nx += dx
            ny += dy

        # 뭘로 while에서 빠져나온지 모르니까 두 조건 다 걸어줘야함
        if 0 < nx < len(board) and 0 < ny < len(board) and board[nx][ny] == c1:
            for i, j in dol:
                board[i][j] = c1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:보드변 길이, M:돌놓는횟수
    board = [[0]*(N + 1) for _ in range(N + 1)]  # 번호 그대로 받으려고 N + 1
    firstset(N, board)

    for _ in range(M):
        x, y, color = map(int, input().split())
        place(x, y, color)

    black = [r.count(1) for r in board]
    white = [r.count(2) for r in board]

    print(f'#{tc} {sum(black)} {sum(white)}')

