import sys
input = sys.stdin.readline


def flatten(lst, num, B):
    time = 0
    required_blocks = 0
    removed_blocks = 0
    for l in lst:
        for i in l:
            tmp = i - num
            if tmp > 0:  # 깎아야할 때
                time += tmp * 2
                removed_blocks += tmp
            elif tmp < 0:  # 쌓아야할 때
                time += abs(tmp)
                required_blocks += abs(tmp)

    if required_blocks <= (removed_blocks + B):
        return time
    else:
        return float('inf')


N, M, B = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

min_time = float('inf')
min_height = -1
for height in range(257):
    current_time = flatten(maps, height, B)
    if current_time <= min_time:
        min_time = current_time
        min_height = height

print(min_time, min_height)
