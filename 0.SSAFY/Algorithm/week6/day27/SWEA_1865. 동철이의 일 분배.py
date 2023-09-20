def work_gogo(work, person, rate):
    global max_rate

    curr_rate = rate * (rates[work][person] / 100)

    if curr_rate < max_rate:  # 확률은 곱할수록 작아지기만 하니까
        return

    visitd[person] = True

    if work == N - 1:
        max_rate = max(max_rate, curr_rate)
        return

    for next_person in range(N):
        if not visitd[next_person]:
            work_gogo(work + 1, next_person, curr_rate)
            visitd[next_person] = False

    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    rates = [list(map(int, input().split())) for _ in range(N)]
    max_rate = 0.0  # 100%

    for person in range(N):
        visitd = [False] * N
        work_gogo(0, person, 1.0)

    print(f'#{tc} {max_rate * 100:.6f}')
