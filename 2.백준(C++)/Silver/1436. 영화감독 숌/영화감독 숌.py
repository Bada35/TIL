N = int(input())
cnt = 0
num = 665

while 1:
    num += 1
    if '666' in str(num):
        cnt += 1

    if cnt == N:
        print(num)
        break
