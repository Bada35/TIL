import sys
input = sys.stdin.readline

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상


# 66퍼 컷..
def move(x, y, cnt=1):
    global max_cnt
    visited.remove(board[x][y])

    if cnt + len(visited) < max_cnt:
        return

    for dx, dy in di:
        is_blocked = True
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] in visited:  # 가용 범위내에 있고, 안 가본 알파벳이면
            is_blocked = False  # 더 이상 못 갈 때만 max_cnt 업데이트
            if cnt + (R - 1 - nx) + (C - 1 - ny) < max_cnt:
                continue
            move(nx, ny, cnt + 1)
        if is_blocked:
            max_cnt = max(max_cnt, cnt)

    visited.add(board[x][y])


R, C = map(int, input().split())  # R행 C열
board = [list(input().strip()) for _ in range(R)]

visited = set(c for row in board for c in row)
max_cnt = float('-inf')

move(0, 0)

print(max_cnt)
