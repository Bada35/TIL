def bitmasking(arr):
    n = len(arr)
    subsets = set()  # 중복제거

    for i in range(1 << n):
        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])

        subsets.add(sum(subset))  # 부분집합 합 set

    return subsets


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())  # N:점원수 B:선반높이
    heights = list(map(int, input().split()))

    sum_subsets = {subset - B for subset in bitmasking(heights) if subset >= B}
    print(f'#{tc} {min(sum_subsets)}')
