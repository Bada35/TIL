for tc in range(1, 11):
    N, s = map(list, input().split())
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            del s[i:i + 2]
            if i != 0:
                i -= 1
        else:
            i += 1
    print('#', tc, ' ', *s, sep='')