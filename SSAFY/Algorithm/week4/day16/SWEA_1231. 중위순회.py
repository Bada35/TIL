def in_order(curr):
    if curr <= N:
        in_order(curr*2)
        print(tree[curr], end='')
        in_order(curr*2+1)


for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    N = int(input())  # N:노드 수
    tree = [''] * (N + 1)

    for i in range(1, N + 1):
        s = input().split()
        tree[i] = s[1]

    in_order(1)
    print()
