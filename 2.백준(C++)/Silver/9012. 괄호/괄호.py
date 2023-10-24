for _ in range(int(input())):
    s = input()
    n = min(s.count(')'), s.count('('))
    for _ in range(n):
        s = s.replace('()', '')
    if s:
        print('NO')
    else:
        print('YES')