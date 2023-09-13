T = int(input())

for tc in range(1, T + 1):
    max_height = 0
    N = int(input())
    heights = list(map(int, input().split()))
    for i in range(N):  # heights 요소 인덱싱
        for j in range(heights[i]):  # 한 height의 1층 2층 3층
            cnt = 0
            for k in range(i + 1, N):  # 그 height보다 낮은 층들에 대해
                if j < heights[k]:
                    cnt += 1
            result = N - 1 - i - cnt
            if result > max_height:
                max_height = result
    print(f'#{tc} {max_height}')
