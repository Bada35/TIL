def pre_order(node):
    if type(tree[node]) == int:  # 숫자면 암것도 안하고 반환
        return tree[node]

    n1 = pre_order(*c1[node]) if c1[node] else 0
    n2 = pre_order(*c2[node]) if c2[node] else 0

    return cal(tree[node], n1, n2)


def cal(op, a, b):  # op:연산자 a:앞값 b:뒤값
    return a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a // b


for tc in range(1, 11):
    N = int(input())  # N:정점의 개수
    tree, c1, c2 = [0], [[] for _ in range(N + 1)], [[] for _ in range(N + 1)]  # c1:왼쪽자식 c2:오른쪽자식
    # 슬라이싱 사용해서 값 할당하려고 c1, c2를 0이 아닌 빈 리스트 집합으로 생성

    for i in range(1, N + 1):
        s = [int(s) if s.isdigit() else s for s in input().split()]
        tree.append(s[1])
        c1[i] = s[2:3]
        c2[i] = s[3:4]

    print(f'#{tc} {pre_order(1)}')
