def CBT(curr, val):
    if curr <= N:  # N번 넘어가면 걍 값만 반환
        val = CBT(curr*2, val)  # 왼쪽 서브트리
        tree[curr] = val
        val += 1
        val = CBT(curr*2+1, val)  # 오른쪽 서브트리
    return val


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # 0쓰기싫어서
    CBT(1, 1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
