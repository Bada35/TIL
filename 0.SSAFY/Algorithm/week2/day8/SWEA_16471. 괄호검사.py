T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    s = [c for c in input() if c in {'{', '}', '(', ')'}]
    print(s)
    i = 0
    while i < len(s)-1:
        if s[i:i + 2] == ['{', '}'] or s[i:i + 2] == ['(', ')']:
            del s[i:i + 2]
            if i != 0:
                i -= 1
        else:
            i += 1
    if len(s):
        print(0)
    else:
        print(1)