# def get_view_good(n, height):
#     result = 0
#     for i in range(2, n - 2):
#         if height[i] > height[i - 2] and height[i] > height[i - 1] and height[i] > height[i + 1] and height[i] > height[i + 2]:
#             result += abs((height[i] - max(height[i - 1],height[i - 2])) - (height[i] - max(height[i + 1], height[i + 2])))
#     return result

def get_view_good(n, height):
    result = 0
    for i in range(2, n - 2):
        max_height = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        if height[i] > max_height:
            result += height[i] - max_height
    return result


for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    print(f'#{tc} {get_view_good(N, heights)}')
