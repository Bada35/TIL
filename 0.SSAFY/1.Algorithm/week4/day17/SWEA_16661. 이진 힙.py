def biHeap(node):
    tree[node] = num.pop(0)
    i = node
    while i//2 >= 1:
        bubble(i, i//2)
        i //= 2


def bubble(n1, n2):  # n1가 자식노드(번호큼) n2가 부모노드(번호작음)
    if not tree[n2] < tree[n1]:  # 부모 노드의 값<자식 노드의 값 아니면
        tree[n1], tree[n2] = tree[n2], tree[n1]  # bubble


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    tree = [0] * (N + 1)

    for i in range(1, N + 1):  # 이진힙 정렬
        biHeap(i)

    # 조상노드 정수합 구하기
    re = 0
    while N > 0:
        re += tree[N // 2]
        N //= 2

    print(f'#{tc} {re}')
