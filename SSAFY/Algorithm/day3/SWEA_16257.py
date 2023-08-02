T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    color = [list(map(int,input().split())) for _ in range(N)]
    # 각 행의 [4]는 색(1은 red, 2는 blue) / [0]은 시작칸 x좌표 [1]은 y좌표 [2]는 끝칸x 좌표 [3]은 끝칸y좌표
    area = [[0] * 10 for _ in range(10)] #10x10 0행렬

    for i in range(N): # 각 행(리스트요소)에 대해 하려고
        for col in range(color[i][0], color[i][2]+1):
            for row in range(color[i][1], color[i][3]+1):
                area[col][row] += color[i][4]

    cnt = 0
    for j in range(10):
        for k in range(10):
            if area[j][k] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
