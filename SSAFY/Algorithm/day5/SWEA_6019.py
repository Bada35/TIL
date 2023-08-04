T = int(input())
for tc in (1, T + 1):
    D, A, B, F = map(int, input().split())
    A_pos, B_pos = 0, D
    result = 0
    # D=250, A=10, B=15, F=20
    # 초속 A=10/360, B=15/360, F=20/360
    while A_pos <= B_pos:
        D = B_pos - A_pos
        cnt = 0
        if cnt == 0:
            result += (D * F) / (B + F)
            B_pos -= (D * B) / (B + F)
            A_pos += (D * A) / (B + F)
            cnt += 1
        else:
            result += (D * F) / (A + F)
            B_pos -= (D * B) / (A + F)
            A_pos += (D * A) / (A + F)
            cnt -= 1
    print(result)







# 지수언니에게
# 배부르니까
# 너무
# 잠온다
# ㅜㅜ