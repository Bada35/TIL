di = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상


def play():  # 유망하지 않을 조건이 뭘까?
    pass


for tc in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]  # join쓸거라 int로 안받음
    nums = set()

    print(f'#{tc} {len(nums)}')