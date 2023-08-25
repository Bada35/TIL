# def CBT(curr, val):
#     if curr <= N:
#         CBT(curr*2, val)
#         tree[curr] = val
#         val += 1
#     pass

def CBT(curr, val):
    if curr <= N:
        val = CBT(curr*2, val)  # 왼쪽 서브트리 탐색
        tree[curr] = val        # 현재 노드에 값 할당
        val += 1                # 값 증가
        val = CBT(curr*2 + 1, val)  # 오른쪽 서브트리 탐색
    return val


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # 0번 계산하기싫어서
    CBT(1, 1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
