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


def cal(op, a, b):  # op: 연산자, a: 앞 값, b: 뒷 값
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:  # 분모가 0인 경우 예외 처리
            return 0  # 이 부분은 문제의 요구 사항에 따라 다르게 처리될 수 있습니다.
        return a // b


for tc in range(1, 11):
    N = int(input())
    tree = [0]

    for i in range(N):  # 정수는 정수로 받기
        s = [int(s) if s.isdigit() else s for s in input().split()]
        tree.append(s[1])

    result = pre_order(1)  # 루트 노드부터 시작
    print(f'#{tc} {result}')
