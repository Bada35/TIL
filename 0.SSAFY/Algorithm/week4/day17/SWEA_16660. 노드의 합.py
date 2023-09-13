def filltree(node):
    i = N
    while i != node:
        tree[i//2] = tree[i] + tree[i+1]
        i -= 1


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # N:노드의개수 M:리프노드개수 L:노드번호
    tree = [0] * (N + 2)  # 자식 1개인경우 index에러 피하려고
    for _ in range(M):
        n, num = map(int, input().split())
        tree[n] = num

    filltree(L)  # L까지만 노드 채우기

    print(f'#{tc} {tree[L]}')