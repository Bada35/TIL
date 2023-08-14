T = int(input())
for tc in range(1, T + 1):
    s = list(input())
    i = 0
    while i < len(s)-1:
        if s[i] == s[i + 1]:
            del s[i:i + 2]
            if i != 0:
                i -= 1
        else:
            i += 1
    print(f'#{tc} {len(s)}')
