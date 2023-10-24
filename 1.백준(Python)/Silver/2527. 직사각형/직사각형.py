import sys
input = sys.stdin.readline


def ser():
    if stx2 > edx1 or sty2 > edy1 or stx1 > edx2 or sty1 > edy2:  # 겹치는게 없는 조건
        return 'd'
    elif (edx1 == stx2 and edy1 == sty2) or (edx1 == stx2 and sty1 == edy2) or (stx1 == edx2 and sty1 == edy2) or (stx1 == edx2 and edy1 == sty2):
        return 'c'
    elif edx1 == stx2 or edx2 == stx1 or edy1 == sty2 or sty1 == edy2:
        return 'b'
    else:
        return 'a'


for _ in range(4):
    stx1, sty1, edx1, edy1, stx2, sty2, edx2, edy2 = map(int, input().split())
    print(ser())


