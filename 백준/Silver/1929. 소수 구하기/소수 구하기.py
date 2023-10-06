s, e = map(int, input().split())
if s == 1:
    s += 1
for n in range(s, e + 1):
    valid = True
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            valid = False
            break
    if valid:
        print(n)
