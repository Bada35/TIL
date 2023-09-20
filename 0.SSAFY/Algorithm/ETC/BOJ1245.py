# 방향배열 : 오른쪽부터 시계방향
di = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


# 전체 heights를 순회하면서 봉우리 개수 세기. dfs
def cnt_peaks():
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                if is_peak(x, y, visited):  # 봉우리라면 cnt + 1
                    cnt += 1
    return cnt


# 봉우리인지 판단
def is_peak(x, y, visited):
    h = heights[x][y]
    stack = [(x, y)]
    is_peak = True  # 초기에는 산봉우리라고 가정
    visited[x][y] = True

    # DFS 시작
    while stack:
        cx, cy = stack.pop()
        for dx, dy in di:
            nx, ny = cx + dx, cy + dy
            # 범위를 벗어나면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 더 높은 지점을 만나면 산봉우리가 아니다.
            if h < heights[nx][ny]:
                is_peak = False

            # 같은 높이고, 아직 방문하지 않은 경우 스택에 추가
            # 같은 높이의 연속된 지점을 산봉우리의 일부로 취급하기 위함
            elif h == heights[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True

    return is_peak


N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

print(cnt_peaks())
