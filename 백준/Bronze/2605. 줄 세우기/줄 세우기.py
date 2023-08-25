import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

stu = []

for i in range(N):
    stu.insert(i-num[i], i + 1)

print(*stu, sep='\n')