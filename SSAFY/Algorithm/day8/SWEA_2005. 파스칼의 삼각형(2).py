T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    li = [1]
    for _ in range(N):
        print(*li)
        new_li = [1]
        for i in range(len(li) - 1):
            new_li.append(li[i] + li[i + 1])
        new_li.append(1)
        li = new_li
