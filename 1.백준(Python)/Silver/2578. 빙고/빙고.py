def fill_bingo(n):
    num_id = Bingo.index(n)
    Bingo.pop(num_id)
    Bingo.insert(num_id, 0)


def bingo_check():
    cnt = 0
    dae1 = []
    dae2 = []

    for i in range(5):
        if Bingo[i::5] == [0, 0, 0, 0, 0]:
            cnt += 1
        if Bingo[5 * i:5 * (i + 1)] == [0, 0, 0, 0, 0]:
            cnt += 1
        dae1.append(Bingo[6 * i])
        dae2.append(Bingo[4 * (i + 1)])

    if dae1 == [0, 0, 0, 0, 0]:
        cnt += 1
    if dae2 == [0, 0, 0, 0, 0]:
        cnt += 1

    return cnt





Bingo = []
Call = []

for i in range(5):
    Bingo += input().split()

for i in range(5):
    Call += input().split()

for num in Call[:11]:
    fill_bingo(num)

for i in range(11, 25):
    fill_bingo(Call[i])
    if bingo_check() >= 3:
        print(i + 1)
        break
