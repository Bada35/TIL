from itertools import combinations

def get_permutation(lst):  # list를 받아서 오름차순인 순열 리스트를 반환
    result = []
    result = [list(comb) for r in range(1, len(lst) + 1) for comb in combinations(lst, r)]
    return result

def get_charge_num(movement, busstop, charger_num, chargers):
    chargers.insert(0, 0)
    chargers.append(busstop)
    perm = get_permutation(chargers)
    result = charger_num

    for i in range(charger_num + 1):
        if (perm[len(perm) - 1][i + 1] - perm[len(perm) - 1][i]) > movement:
            return 0

    for j in perm:
        for k in range(len(j) - 1):
            if (j[k + 1] - j[k]) > movement:  # 만족 못하는 순간 다음 순열로
                break
        if (len(j) - 2) < result:
            result = len(j) - 2

    return result


T = int(input())

for tc in range(1, T + 1):
    KNM = list(map(int, input().split()))
    busstops = list(map(int, input().split()))
    print(f'#{tc} {get_charge_num(KNM[0], KNM[1], KNM[2], busstops)}')
