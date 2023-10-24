import sys
input = sys.stdin.readline

di = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # 우 부터 시계방향

def cnt_peaks():
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                if is_peak(x, y, visited):
                    cnt += 1
    return cnt

def is_peak(x, y, visited):
    h = heights[x][y]
    stack = [(x, y)]
    is_peak = True
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        for dx, dy in di:
            nx, ny = cx + dx, cy + dy
            # 범위를 벗어나는 경우는 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 주변에 더 높은 곳이 있다면 봉우리가 아님
            if h < heights[nx][ny]:
                is_peak = False
            # 주변에 높이가 같은 곳이 있고 아직 방문하지 않았다면 스택에 추가
            elif h == heights[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True

    return is_peak

N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]

print(cnt_peaks())
