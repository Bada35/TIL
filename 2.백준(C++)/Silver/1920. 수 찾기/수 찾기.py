import sys
input = sys.stdin.readline

input()
li = set(map(int, input().split()))
n = int(input())
li2 = list(map(int, input().split()))
for i in li2:
    if i in li:
        print(1)
    else:
        print(0)
