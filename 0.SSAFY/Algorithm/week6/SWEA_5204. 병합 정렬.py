def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    if sorted_left[-1] > sorted_right[-1]:  # 왼쪽 마지막 원소 > 오른쪽 마지막 원소보
        cnt += 1

    return merge2(sorted_left, sorted_right)


def merge2(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    sorted_nums = merge_sort(nums)
    print(f'#{tc} {sorted_nums[N//2]} {cnt}')