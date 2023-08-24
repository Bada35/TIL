decode = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}


def str2code(s):
    last_id = s.rfind('1')
    return [decode[int(s[i:i + 7], 2)] for i in range(last_id - 55, last_id + 1, 7)]


def isvalid(code):
    odd = code[::2]
    even = code[1::2]
    if not (sum(odd) * 3 + sum(even)) % 10:  # 조건 맞으면 합 반환
        return sum(code)
    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    s = [input() for _ in range(N)]

    codes = next((r for r in s if '1' in r), '')

    print(f'#{tc} {isvalid(str2code(codes))}')


