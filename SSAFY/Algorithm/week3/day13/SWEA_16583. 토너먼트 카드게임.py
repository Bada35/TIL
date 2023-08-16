def rsp(n1, n2):
    if hand[n1] == hand[n2]:
        return min(n1, n2)
    elif (hand[n1], hand[n2]) in [(1, 3), (3, 2), (2, 1)]:
        return n1
    else:
        return n2

def tourna(lst):
    l = len(lst)
    if l == 1:
        return lst[0]
    mid = (l + 1) // 2
    win1 = tourna(lst[:mid])
    win2 = tourna(lst[mid:])
    return rsp(win1, win2)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    hand = list(map(int, input().split()))
    print(f'#{tc} {tourna(range(N)) + 1}')