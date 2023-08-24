decode = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}


def hex2bi(s):  # 받아온 str 행을 2진코드로 변경한 뒤, rstrip을 통해 뒤쪽 0 제거
    s = ''.join(format(int(c, 16), '04b') for c in s)  # '8E' -> '10001110'
    return s.rstrip('0')


def find_code(s):  # 받은 str에서 가능한 암호코드를 list화해서 반환
    lst = []
    while s:
        for l in range(1, 6):  # 최대 5배수
            si = s[len(s) - 56*l::l]
            try:
                lst.append(bi2de(si))
                s = s[:len(s) - 56*l]
                s = s.rstrip('0')
                if not s:
                    break
            except KeyError:
                continue

    return lst  # return list : 한 줄에 여러 개일 수 있어서 [[정수 암호코드],[정수 암호코드]]


def bi2de(s):  # s:잘린str, l:배수
    lst = []
    # print(f'bi2code {s}')
    for i in range(0, 56, 7):
        lst.append(decode[int(s[i:i + 7], 2)])
    return lst


def isvalid(code):
    odd = code[::2]
    even = code[1:7:2]
    certi = code[-1]
    if not (sum(odd)*3 + sum(even) + certi) % 10:  # 조건 맞으면 합 반환
        return sum(code)
    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:배열의 세로 크기 M:배열의 가로크기(1≤N<2000, 1≤M<500).
    c = list({i.strip() for i in [input() for _ in range(N)] if any(c != '0' for c in i)})
    # 0이 없는 입력 행을 받아와서, list({})를 통해 중복 제거
    # c = ['01E06079861E79F99FE079861E79F800000', '00000006EED19376EC58D0000000000'] 이런식

    cd = []  # cd = [[정수 암호코드],[정수 암호코드]] 로 저장할거(중복 o)
    for i in c:
        i = hex2bi(i)
        cd += find_code(i)

    codes = []
    for c in cd:  # 중복 제거
        if c not in codes:
            codes.append(c)
    print(codes)

    res = 0
    for j in codes:
        res += isvalid(j)

    print(f'#{tc} {res}')






