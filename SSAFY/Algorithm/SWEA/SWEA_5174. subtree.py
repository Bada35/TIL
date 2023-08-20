def bTree(root):
    global cnt
    cnt += 1

    if root not in tree:
        return

    for sub in tree[root]:
        bTree(sub)

'''
def count_subtree(node):
    if not tree.get(node): # 자식 노드가 없는 경우
        return 1
    count = 1 # 현재 노드 포함
    for child in tree[node]:
        count += count_subtree(child)
    return count
'''

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    e = list(map(int, input().split()))

    tree = {}
    for i in range(0, len(e), 2):
        if e[i] not in tree:
            tree[e[i]] = []
        tree[e[i]].append(e[i + 1])

    cnt = 0
    bTree(N)
    print(f'#{tc} {cnt}')




