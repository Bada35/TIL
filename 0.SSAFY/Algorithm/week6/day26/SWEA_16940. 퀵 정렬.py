def quick_sort(li):
    if len(li) <= 1:  # ==하면 []에서 error
        return li

    pivot = li[len(li)//2]

    left = [n for n in li if n < pivot]
    middle = [n for n in li if n == pivot]  # 같은수 있읋수도 있으니까
    right = [n for n in li if n > pivot]

    return quick_sort(left) + middle + quick_sort(right)


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = quick_sort(nums)

    print(f'#{tc} {sorted_nums[N // 2]}')