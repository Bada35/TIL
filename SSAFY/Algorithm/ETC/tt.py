zero_coor = [(0, 0), (1, 4), (1, 7), (2, 0), (2, 2), (3, 3), (4, 1), (4, 7), (5, 5), (6, 6), (6, 8), (7, 1), (7, 4), (8, 8)]
zero_can = [set() for _ in range(len(zero_coor))]
zero_can[1].add(1)

print(zero_can)



def init():
    for x, y in zero_coor:
        sudo[x][y] = set(i for i in range(1, 10))
        for i in range(9):
            if not type(sudo[x][i]) == set:
                sudo[x][y].discard(sudo[x][i])
            if not type(sudo[i][y]) == set:
                sudo[x][y].discard(sudo[i][y])

        box_x, box_y = (x // 3) * 3, (y // 3) * 3
        for j in range(box_x, box_x + 3):
            for k in range(box_y, box_y + 3):
                if not type(sudo[j][k]) == set:
                    sudo[x][y].discard(sudo[j][k])