A, B, V = map(int, input().split())
h, cnt = 0, 0

res = (V - A) // (A - B) + 1
if (V - A) % (A - B):
    res += 1

print(res)