def dump(lst):
    lst[lst.index(max(lst))] -= 1
    lst[lst.index(min(lst))] += 1


for tc in range(10):
    dumps = int(input())
    box_heights = list(map(int, input().split()))

    print(f'#{tc+1}',end=' ')
    while dumps > 0:
        if max(box_heights)-min(box_heights) <= 1:
            print(max(box_heights)-min(box_heights))
            break
        else:
            dump(box_heights)
            dumps -= 1
    print(max(box_heights)-min(box_heights))
