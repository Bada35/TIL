T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # N:노드개수 M:리프노드개수 L:출력노드번호
    tree = [0] * (N + 1)

    for _ in range(M):
        n, num = map(int, input().split())
        tree[n] = num

    for i in range(N - M, 0, -1):
        try:
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
        except IndexError:
            tree[i] = tree[i * 2]

    print(f'#{tc} {tree[L]}')
