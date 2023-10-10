judge = []
for _ in range(int(input())):
    i, j = input().split()
    judge.append((int(i), j))

judge.sort(key=lambda x: x[0])
for i in judge:
    print(*i)