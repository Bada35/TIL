def fill_bingo(n):
    num_id = Bingo.index(n)
    Bingo.pop(num_id)
    Bingo.insert(num_id, 0)  # 부른건 0 표시


def bingo_check():
    cnt = 0
    dae1 = []
    dae2 = []

    #가로 체크
    for i in range(5):
        if Bingo[i::5] == [0, 0, 0, 0, 0]:
            # print('세로카운트+1')
            cnt += 1
        if Bingo[5 * i:5 * (i + 1)] == [0, 0, 0, 0, 0]:
            # print('가로카운트+1')
            cnt += 1
        dae1.append(Bingo[6 * i])
        dae2.append(Bingo[4 * (i + 1)])

    if dae1 == [0, 0, 0, 0, 0]:
        cnt += 1
        # print('대1카운트+1')
    if dae2 == [0, 0, 0, 0, 0]:
        cnt += 1
        # print('대2카운트+1')

    return cnt





Bingo = []
Call = []

for i in range(5):
    Bingo += input().split()

for i in range(5):
    Call += input().split()

# print(Bingo)
# print(Call)

# for num in Call[:12]:  # 12번까진 일단 부르기(그전엔 빙고 안됨)
#     fill_bingo(num)

for i in range(25):
    fill_bingo(Call[i])
    # for i in range(5):
    #     print(Bingo[5*i:5*(i+1)])
    # print(bingo_check())
    if bingo_check() >= 3:
        print(i + 1)
        break
