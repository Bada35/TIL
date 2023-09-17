def sudoku():  # 확실하게 채울 수 있는건 채우고, bt로 채우는 함수
    init()
    backtrack(0)  # 백트래킹 시작


def backtrack(index):  # 백트래킹 함수
    if index == len(zero_coor):  # 모든 빈 칸을 채운 경우
        return True

    x, y = zero_coor[index]

    for num in range(1, 10):  # 1부터 9까지 시도
        if is_valid(x, y, num):
            sudo[x][y] = num
            if backtrack(index + 1):  # 다음 빈칸으로
                return True
            sudo[x][y] = 0  # 실패하면 원래대로
    return False


def is_valid(x, y, num):  # 유효성 검사 함수
    for i in range(9):
        if sudo[x][i] == num:
            return False
        if sudo[i][y] == num:
            return False

    box_x, box_y = (x // 3) * 3, (y // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if sudo[i][j] == num:
                return False
    return True


def init():  # 채울 수 있는건 채우는 함수
    zero_can = [set(i for i in range(1, 10)) for _ in range(len(zero_coor))]
    cnt = 0
    for x, y in zero_coor:
        for i in range(9):
            zero_can[cnt].discard(sudo[x][i])
            zero_can[cnt].discard(sudo[i][y])
        box_x, box_y = (x // 3) * 3, (y // 3) * 3
        for j in range(box_x, box_x + 3):
            for k in range(box_y, box_y + 3):
                zero_can[cnt].discard(sudo[j][k])
        cnt += 1
    # print(zero_can)

    while not all(len(l) != 1 for l in zero_can):
        for i in range(len(zero_can)):
            if len(zero_can[i]) == 1:
                x, y, num = zero_coor[i][0], zero_coor[i][1], zero_can[i].pop()
                sudo[x][y] = num
                zero_can.pop(i)
                zero_coor.pop(i)
                update(x, y, num, zero_can)
                break


def update(x, y, n, lst):  # 확실하게 채울거 채우고나서 후보군 업데이트
    cnt = 0
    for nx, ny in zero_coor:
        if nx == x:
            lst[cnt].discard(n)
        if ny == y:
            lst[cnt].discard(n)
        if (x // 3 == nx // 3) and (y // 3 == ny // 3):
            lst[cnt].discard(n)
        cnt += 1


sudo = [list(map(int, input().split())) for _ in range(9)]
zero_coor = []  # 비어있는 자리 튜플로 추가
# print(sudo)

for i in range(9):
    for j in range(9):
        if not sudo[i][j]:
            zero_coor.append((i, j))

# print(zero_coor)

sudoku()
for i in sudo:
    print(*i)
