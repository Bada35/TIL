# def cal_fee(months):
#     fee = [day_fee(months), month1_fee(months), min(fees), year_fee(months)]
#     print(fees)
#     return min(fee)
#
#
# def day_fee(months):
#     return sum([m * Fees[0] for m in months])
#
#
# def month1_fee(months):
#     return len(months) * Fees[1]
#
#
# def month3_fee(months, curr_sum=0, id=0):  # 연속만 고려, 재귀로 구현 약간 dfs처럼?
#     global fees
#
#     if not months:  # 슬라이싱으로 빈 배열 넘어오면
#         fees.append(curr_sum)
#         return
#
#     fees.append(curr_sum + min(day_fee(months), month1_fee(months)))  # 나머지 분기로 안나눴을경우도 넣기
#     curr_sum += Fees[2]  # 분기로 나눴을경우
#     months = months[3:]
#
#
#     month3_fee()
#
#
# def year_fee(months):
#     if len(months) != 12:
#         return float('inf')
#     return Fees[3]
def cal_fee(months):
    pay = [0 for _ in range(13)]

    for i in range(13):
        pay[i] = min(months[i] * Fees[0], Fees[1]) + pay[i - 1]
        if i > 2:
            pay[i] = min(pay[i], Fees[2] + pay[i - 3])

    return min(Fees[3], pay[12])


for tc in range(1, int(input()) + 1):
    Fees = list(map(int, input().split()))  # 0:일요금 1:한달요금 2:세달요금 3:연요금
    months = [0] + list(map(int, input().split()))

    print(f'#{tc} {cal_fee(months)}')


# T = int(input())
# for tc in range(1, T+1):
#     price = list(map(int, input().split()))
#     plan = [0] + list(map(int, input().split()))
#     expense = [0 for _ in range(13)]
#
#     for i in range(1, 13):
#         # 하루, 한달 비교
#         expense[i] = min(plan[i] * price[0], price[1]) + expense[i-1]
#         # 3개월 이상부터 3달까지 비교
#         if i > 2:
#             expense[i] = min(expense[i], price[2] + expense[i-3])
#     # 1년 비교
#     ans = min(expense[12], price[3])
#     print(f'#{tc} {ans}')

