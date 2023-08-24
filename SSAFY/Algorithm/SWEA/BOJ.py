import sys
input = sys.stdin.readline


def fillbingo(n):
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == n:
                bingo[x][y] = 0
                return


def check():
    cnt = 0
    cnt1 = 1
    cnt2 = 1
    for x in range(5):
        cnt += 1
        if bingo[x].count(0) == 5:
            cnt += 1
        for y in range(5):
            if bingo[y][x]:
                cnt -= 1
                break

    for i in range(5):
        if bingo[i][i]:
            cnt1 = 0
        if bingo[i][4-i]:
            cnt2 = 0

    cnt += cnt1
    cnt += cnt2

    if cnt >= 3:
        return 1
    return 0


bingo = []
call = []
res = 0
for _ in range(5):
    bingo.append(input().split())
for _ in range(5):
    s = input().split()
    call += s

print(*bingo, sep='\n')
print(call)

for i in call[:12]:  # 12까진 일단 불러야함
    fillbingo(i)

for j in range(12, 25):
    fillbingo(call[j])
    if check():
        res = j + 1
        break

print(res)
