def babygin(t1, t2):
    global winner
    pl1.append(nums[t1])
    pl2.append(nums[t2])

    if runn(pl1) or triple(pl1):
        winner = 1
        return 1
    if runn(pl2) or triple(pl2):
        winner = 2
        return 1

    return 0


def runn(lst):
    lst = list(set(lst))
    lst.sort()
    for i in range(len(lst) - 2):
        if lst[i] + 1 == lst[i + 1] and lst[i + 1] + 1 == lst[i + 2]:
            return 1
    return 0


def triple(lst):
    for i in lst:
        if lst.count(i) >= 3:
            return 1
    return 0


T = int(input())

for tc in range(1, T + 1):
    nums = list(map(int, input().strip().split()))

    pl1, pl2 = nums[:4:2], nums[1:4:2]
    winner = 0

    for i in range(4, 12, 2):
        babygin(i, i + 1)
        if winner:
            break

    print(f'#{tc} {winner}')


