def bt(r, s):  # r = row 열
    global min_sum

    if r == N:  # 다 탐색했으면 지금 sum이랑 min_sum중 작은거 min_sum에 넣기
        min_sum = min(s, min_sum)
        return

    if s >= min_sum:
        return

    for c in range(N):  # c = col 행
        if not visited[c]:
            visited[c] = True
            bt(r+1, s + n[r][c])
            visited[c] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000
    visited = [False] * N  # 행 방문했는지 확인용
    bt(0, 0)

    print(f'#{tc} {min_sum}')