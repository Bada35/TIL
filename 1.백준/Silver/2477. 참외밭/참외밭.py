T = int(input())  # T:단위면적당 참외개수
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4

length = []

for _ in range(6):
    d, l = map(int, input().split())
    length.append(l)


mx_len1 = max(length)
mx_id1 = length.index(mx_len1)
if length[mx_id1 - 1] > length[(mx_id1 + 1) % 6]:
    mx_len2 = length[mx_id1 - 1]
    mx_id2 = mx_id1 - 1
else:
    mx_len2 = length[(mx_id1 + 1) % 6]
    mx_id2 = mx_id1 + 1
idd = max(mx_id1, mx_id2) % 6

area = mx_len1 * mx_len2 - length[(idd + 2) % 6] * length[(idd + 3) % 6]

print(area * T)
