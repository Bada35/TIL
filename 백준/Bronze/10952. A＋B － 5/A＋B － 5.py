A, B = 1, 1
while 1:
    A, B = map(int, input().split())
    if A == 0 or B == 0:
        break
    print(A+B)
