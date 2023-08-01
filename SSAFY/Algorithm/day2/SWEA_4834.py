T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    card_cnt = [0] * 10

    for card in cards:
        card_cnt[card] += 1
    max_card = 9 - card_cnt[::-1].index(max(card_cnt))
    print(f'#{tc} {max_card} {max(card_cnt)}')
