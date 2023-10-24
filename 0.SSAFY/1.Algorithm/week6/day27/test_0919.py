def work_gogo(cnt, curr=100):
    global max_rate

    if curr <= max_rate:
        return

    if cnt >= N:
        max_rate = curr
        return

    else:
        for i in range(N):

            if not visited[i]:
                if not rates[cnt][i]:
                    continue
                visited[i] = True
                work_gogo(cnt+1, curr * (rates[cnt][i]))
                visited[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())

    rates = [list(map(lambda x : int(x)/100,input().split())) for _ in range(N)]

    visited = [False] * N
    max_rate = float('-inf')
    work_gogo(0)

    print(f'#{tc} {max_rate:6f}')