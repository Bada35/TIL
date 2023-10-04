tmp = 1
for i in range(1, int(input()) + 1):
    tmp *= i

s = str(tmp)
cnt = 0
l = len(s)

for i in range(l - 1, -1, -1):
    if s[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break
