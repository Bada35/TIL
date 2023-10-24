from sys import stdin
input = stdin.readline


def make_floor(fl):
    li = [[0] * 14 for _ in range(max(floor) + 1)]
    li[0] = [i for i in range(1, 15)]
    for i in range(1, fl + 1):
        for j in range(14):
            li[i][j] = sum(li[i-1][:j + 1])
    # print(li)
    return li


floor, ho = [], []
tc = int(input())


for _ in range(tc):
    floor.append(int(input()))
    ho.append(int(input()))

residents = make_floor(max(floor))

for i in range(tc):
    print(residents[floor[i]][ho[i] - 1])
