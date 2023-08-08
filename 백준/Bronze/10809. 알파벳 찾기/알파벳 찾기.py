S = input()
li = []
for i in range(ord('a'), ord('z')+1):
    li.append(S.find(chr(i)))
print(*li)
