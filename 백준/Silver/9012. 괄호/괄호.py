for _ in range(int(input())):
    s = input()
    n = s.count('(')
    for _ in range(n):
        s = s.replace('()', '')
    if s:
        print('NO')
    else:
        print('YES')