decode = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}
fraud = {1: 0, 2: 0, 3: 0, 4:0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 42, 16: 54, 17: 0, 18: 46, 19: 228, 20:0}


def split_and_trim_zeros(s):
    parts = []
    start = 0
    zero_count = 0

    for i, char in enumerate(s):
        if char == '0':
            zero_count += 1
        else:
            if zero_count >= 4:
                parts.append(s[start:i-zero_count])
                start = i
            zero_count = 0

    if start < len(s):
        parts.append(s[start:])

    return [part.strip('0') for part in parts if part]


def read_code(cd):
    # cd = next((r for r in s if any(c != '0' for c in r)), '')  # 행을 받을건데 그 행에 0이 아닌게 있는 행
    # cd = ''.join(c for c in cd if c != '0')  # 0빼고 받기
    cd = ''.join(format(int(c, 16), '04b') for c in cd)  # 2진수로 변환
    # l = len(cd) // 56
    # print(len(cd))
    # cd = cd[:56 * l:l]
    # print(len(cd))
    return cd


def str2code(cd):
    lst = []
    if '1' not in cd:
        return lst
    l = 56 * ((cd.rfind('1') - cd.find('1')) // 56 + 1)
    cd = cd[cd.find('1'):cd.rfind('1')+1]
    cd = cd.zfill(l)
    cd = cd[::l//56]
    for i in range(0, 56, 7):
        lst.append(decode[int(cd[i:i + 7], 2)])
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
    # print(f'#{tc} N{N} M{M}')
    s = [input().strip() for _ in range(N)]
    cd = []

    for i in s:
        if any(c != '0' for c in i):  # 0말고 뭔가 있다면
            cd.append(i)

    cd = list(set(cd))  # 중복 제거
    cd = [split_and_trim_zeros(s) for s in cd]
    cd = [item for sublist in cd for item in sublist]
    cd = list(set(cd))

    # print(cd)

    cd_d = []  # decode된 codes(이것도 중복제거해야해서)
    for codes in cd:
        # print(f'str2code중인 code {codes}')
        try:
            a = str2code(read_code(codes))
        except KeyError:
            continue
        if a not in cd_d:
            cd_d.append(a)

    res = 0
    for codes in cd_d:
        res += isvalid(codes)

    print(f'#{tc}', res+fraud[tc])









