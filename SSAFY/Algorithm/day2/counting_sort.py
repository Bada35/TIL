array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 주어진 배열의 max+1개만큼 칸 가진 count 생성
count = [0] * (max(array) + 1)

# 7 만나면 count[7] 값 +1 하는식으로
# count[i] 값에 array내 i 값의 개수 저장
for i in array:
    count[i] += 1 # count = [2, 2, 2, 1, 1, 2, 1, 1, 1, 2]

array.clear()

# count의 요소 개수 = max(array)+1 = (0~9) 동안 출력 j
# 그 j를 몇 번 출력하냐면, array 내 값의 개수인 count[j]만큼
for j in range(len(count)):
    for k in range(count[j]):
        array.append(j)

print(array)
