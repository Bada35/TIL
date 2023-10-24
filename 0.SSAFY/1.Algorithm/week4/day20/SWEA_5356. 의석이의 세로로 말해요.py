T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    word = [input() for _ in range(5)]
    max_l = 0

    for w in word:
        max_l = max(max_l, len(w))

    for i in range(max_l):
        for j in range(5):
            try:
                print(word[j][i], end='')
            except IndexError:
                continue
    print()
