cnt = 1
target = int(input())

layer = 1
bae = 6

while 1:
    if target <= layer:
        print(cnt)
        break
    layer += bae
    bae += 6
    cnt += 1
