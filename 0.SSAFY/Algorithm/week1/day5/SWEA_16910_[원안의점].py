T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    CT = [N, N]
    cnt = 0
    for c in range(N*2+1):
        for r in range(N*2+1):
            if (c - CT[0])**2 + (r - CT[1])**2 <= N**2:
                cnt += 1

    print(f'#{tc} {cnt}')