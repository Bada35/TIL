import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # N:학생수 K:방최대인원
student = [[0]*6 for _ in range(2)]

for _ in range(N):
    s, g = map(int, input().split())
    student[s][g-1] += 1

student = student[0] + student[1]

res = 0
for stu in student:
    res += (stu + K - 1) // K

print(res)