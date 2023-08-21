def dfs(node):
    if not adj_lst[node]:
        return 1
    cnt = 1
    for sub in adj_lst[node]:
        cnt += dfs(sub)

    return cnt


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E:간선개수 N:시작노드
    s = list(map(int, input().split()))
    adj_lst = [[] for _ in range(E + 2)]  # 노드 번호 1부터 E+1까지 있다고 했으니까

    for i in range(0, len(s), 2):
        adj_lst[s[i]].append(s[i + 1])

    print(f'#{tc} {dfs(N)}')
