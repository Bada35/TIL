def pre_order(node):
    if node > N:
        return 0

    left_child, right_child = node * 2, node * 2 + 1

    if tree[node] in ['+', '-', '*', '/']:
        a = pre_order(left_child)  # 왼쪽 서브트리 결과
        b = pre_order(right_child)  # 오른쪽 서브트리 결과
        return cal(tree[node], a, b)
    else:
        return tree[node]


def cal(op, a, b):  # op:연산자 a:앞값 b:뒤값
    return a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a // b if op == '/' and b != 0 else 0



for tc in range(1, 11):
    N = int(input())
    tree = [0]

    for i in range(N):  # 정수는 정수로 받기
        s = [int(s) if s.isdigit() else s for s in input().split()]
        tree.append(s[1])

    result = pre_order(1)  # 루트 노드부터 시작
    print(f'#{tc} {result}')
