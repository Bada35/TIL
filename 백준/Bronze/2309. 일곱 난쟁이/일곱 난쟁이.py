import sys
input = sys.stdin.readline

nan = []
for _ in range(9):
    nan.append(int(input()))

sub = sum(nan) - 100
nan.sort()

for i in range(8):
    for j in range(i+1, 9):
        if sub == nan[i] + nan[j]:
            nan.pop(i)
            nan.pop(j-1)
            break
    if len(nan) == 7:
        break

print(*nan, sep='\n')
