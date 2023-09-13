A, B = map(int, input().split())
def a(c, d):
    return '<' if c < d else '>' if c > d else '=='
print(a(A,B))