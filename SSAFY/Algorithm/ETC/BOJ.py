def sudoku():  # 확실하게 채울 수 있는건 채우고, bt로 채우는 함수
    init()


def init():
    pass


def fillin():
    pass


sudo = [list(map(int, input().split())) for _ in range(9)]
zero_coor = []  # 비어있는 자리 튜플로 추가
print(sudo)

for i in range(9):
    for j in range(9):
        if not sudo[i][j]:
            zero_coor.append((i, j))

print(zero_coor)

sudoku()
for i in sudo:
    print(*i)
