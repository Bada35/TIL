def is_valid(x, y, num, board):
    if num in board[x]:
        return False

    if num in [board[i][y] for i in range(9)]:
        return False

    box_x, box_y = (x // 3) * 3, (y // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if board[i][j] == num:
                return False

    return True


def sudoku(board, zero_coor, idx):
    if idx == len(zero_coor):
        for row in board:
            print(*row)
        exit(0)

    x, y = zero_coor[idx]

    for num in range(1, 10):
        if is_valid(x, y, num, board):
            board[x][y] = num
            sudoku(board, zero_coor, idx + 1)
            board[x][y] = 0


sudo = [list(map(int, input().split())) for _ in range(9)]
zero_coor = []  # 비어있는 자리 튜플로 추가

for i in range(9):
    for j in range(9):
        if not sudo[i][j]:
            zero_coor.append((i, j))

sudoku(sudo, zero_coor, 0)
for i in sudo:
    print(*i)





# def sudoku():  # 확실하게 채울 수 있는건 채우고, bt로 채우는 함수
#     init()
#
#
# def init():
#     lst = []
#
#     for x, y in zero_coor:
#         lst.append(fillin(x, y))
#
#     for i in range(len(zero_coor)):
#         if not sudo[zero_coor[i][0]][zero_coor[i][1]]:
#             sudo[zero_coor[i][0]][zero_coor[i][1]] = lst[i]
#
#
# def fillin(x, y):
#     s = set()
#
#     for i in range(9):
#         s.add(sudo[x][i])
#         s.add(sudo[i][y])
#
#     for j in range((x // 3) * 3, (x // 3) * 3 + 3):
#         for k in range((y // 3) * 3, (y // 3) * 3 + 3):
#             s.add(sudo[j][k])
#
#     lst = [l for l in range(1, 10) if l not in s]
#     if len(lst) == 1:
#         sudo[x][y] = lst[0]
#         return []
#     else:
#         return lst
#
#
# sudo = [list(map(int, input().split())) for _ in range(9)]
# zero_coor = []  # 비어있는 자리 튜플로 추가
#
# for i in range(9):
#     for j in range(9):
#         if not sudo[i][j]:
#             zero_coor.append((i, j))
#
# sudoku()
# for i in sudo:
#     print(*i)
