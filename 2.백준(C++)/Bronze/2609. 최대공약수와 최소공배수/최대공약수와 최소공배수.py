n1, n2 = map(int, input().split())
if n1 < n2:
    n1, n2 = n2, n1

for i in range(n2, 0, -1):
    if not n1 % i and not n2 % i:
        print(i)
        break
i = 1
while 1:
    if not (n1 * i) % n2:
        print(n1 * i)
        break
    i += 1