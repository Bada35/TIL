import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def preorder_return(val, node, c1, c2, id=1, left=float('-inf'), right=float('inf')):
    if not val:
        return

    num = val[0]
    if num < left or num > right:
        return

    val.pop(0)
    node[id] = num

    # 왼쪽 자식 노드 처리
    c1[id] = id * 2
    preorder_return(val, node, c1, c2, c1[id], left, num)

    # 오른쪽 자식 노드 처리
    c2[id] = id * 2 + 1
    preorder_return(val, node, c1, c2, c2[id], num, right)


def postorder(node, c1, c2, id):
    if id not in node:
        return

    postorder(node, c1, c2, c1.get(id, None))
    postorder(node, c1, c2, c2.get(id, None))
    print(node[id])


val = []
while True:
    try:
        val.append(int(input().strip()))
    except EOFError:
        break

node = {}
c1 = {}
c2 = {}
preorder_return(val, node, c1, c2)
postorder(node, c1, c2, 1)
