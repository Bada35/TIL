from sys import stdin
input = stdin.readline

N = int(input())
person = []

for _ in range(N):
    # w, h = map(input().split())
    person.append(tuple(map(int, input().split())))

for w, h in person:
    cnt = 1
    for w2, h2 in person:
        if w2 > w and h2 > h:
            cnt += 1
    print(cnt, end=' ')
