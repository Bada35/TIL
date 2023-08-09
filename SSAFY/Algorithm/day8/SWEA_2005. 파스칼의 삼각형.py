T = int(input())


def pascal(li, n):
    if len(li) == 1:
        print('1\n1 1')
        return pascal([1, 1], n)
    elif len(li) == n:
        return 0
    li_2 = [1]
    for i in range(len(li) - 1):
        li_2.append(li[i] + li[i + 1])
    li_2.append(1)
    print(*li_2)
    return pascal(li_2, n)


for tc in range(1, T + 1):
    N = int(input())
    pascal([1], N)
