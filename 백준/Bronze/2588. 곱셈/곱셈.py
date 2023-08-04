a = int(input())
b = list(map(int, input()))
r = 0

for i in range(3):
    print(a * b[2-i])
    r += b[2-i] * (10 ** i)
print(a*r)