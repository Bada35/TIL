import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def preorder_return(val, node, id=1, left=float('-inf'), right=float('inf')):
    if not val or id >= len(node):
        return

    num = val[0]

    if num < left or num > right:
        return

    val.pop(0)
    node[id] = num

    preorder_return(val, node, id * 2, left, num)
    preorder_return(val, node, id * 2 + 1, num, right)


def postorder(id):
    if node[id]:
        postorder(id * 2)
        postorder(id * 2 + 1)
        print(node[id])


val = []
while 1:
    try:
        val.append(int(input().strip()))
    except EOFError:
        break
# print(val)

node = [None for _ in range(2**len(val))]
preorder_return(val, node)
postorder(1)