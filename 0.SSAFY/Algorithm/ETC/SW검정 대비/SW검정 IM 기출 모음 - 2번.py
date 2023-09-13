import sys
input = sys.stdin.readline


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    sq = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1
    area = []

    for c in range(N):
        for r in range(N):
            for c1 in range(c, N):
                for r1 in range(r, N):
                    if sq[c][r] != sq[c1][r1]:
                        continue
                    area.append((c1 - c + 1) * (r1 - r + 1))

    print(f'#{tc} {area.count(max(area))}')

