from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    N, idx = map(int, input().split())
    books = deque(list(map(int, input().split())))
    cnt = 0

    while True:
        if max(books) == books[0]:
            cnt += 1
            books.popleft()
            if idx == 0:
                print(cnt)
                break
            else:
                idx -= 1
        else:
            if idx == 0:
                idx = len(books) - 1
            else:
                idx -= 1
            books.rotate(-1)

