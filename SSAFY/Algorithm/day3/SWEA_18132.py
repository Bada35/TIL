T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):  # 1<<n = 2ⁿ 즉 부분 집합의 개수만큼
        subset = []
        for j in range(12):  # 원소의 수 만큼 비트를 비교함
            if i & (1 << j):  # for i in range(n):\n if bit[i]: 과 같은역할
                subset.append(A[j])
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print(f'#{tc} {cnt}')
