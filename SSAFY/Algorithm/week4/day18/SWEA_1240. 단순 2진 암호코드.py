decode = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}


def str2code(s):  # main함수 codes가 들어있는 str을 [해독된 정수1, 해독된 정수2, ...] 로 return
    lst = []
    last_id = s.rfind('1')  # 1 마지막 위치
    for i in range(last_id-55, last_id+1, 7):  # [ 0111011, 0110001, ... ] 되도록 자른 후
        lst.append(decode[int(s[i:i+7], 2)])  # 해독해서 append
    return lst


def isvalid(code):  # code는 list로 받기
    odd = code[::2]
    even = code[1::2]
    if not (sum(odd)*3 + sum(even)) % 10:  # 조건 맞으면 합 반환
        return sum(code)
    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:배열의 세로 크기 M:배열의 가로크기 (1≤N≤50, 56≤M≤100)
    s = [input() for _ in range(N)]

    for i in s:
        if not i.find('1') == -1:  # '1'이 있는 행이라면
            codes = i
            break
    # 쓸데없이 돌아가는거 나중에 줄이기

    print(f'#{tc} {isvalid(str2code(codes))}')


