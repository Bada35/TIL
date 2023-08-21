def inorder(node):
    pass


def iscal():
    pass


for tc in range(1, 11):
    N = int(input())  # N:정점수
    tree = [0]
    for _ in range(N):
        s = input().split()
        tree += s[1]

    print(f'#{tc} {iscal()}')
