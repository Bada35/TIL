def isvalid(sam, pas):
    for j in pas:
        if j in sam:
            sam = sam[sam.index(j)+1:]
        else:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N:Sample의 길이, K:PassCode의 길이
    sample = input().split()
    passcode = input().split()

    i = 0
    while i < len(sample) - 1:
        if sample[i] == sample[i + 1]:
            sample.pop(i)
        else:
            i += 1

    print(f'#{tc} {int(isvalid(sample, passcode))}')


#
# # 시간복잡도 개선
# def isvalid(sam, pas):
#     idx = 0
#     for j in pas:
#         try:
#             new_idx = sam.index(j, idx)
#             idx = new_idx + 1
#         except ValueError:
#             return False
#     return True
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     sample_raw = input().split()
#     passcode = input().split()
#
#     # 중복된 요소를 제거
#     sample = [sample_raw[0]]
#     for i in range(1, len(sample_raw)):
#         if sample_raw[i] != sample_raw[i - 1]:
#             sample.append(sample_raw[i])
#
#     print(f'#{tc} {int(isvalid(sample, passcode))}')
