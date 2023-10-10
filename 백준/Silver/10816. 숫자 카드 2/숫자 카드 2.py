from collections import Counter
import sys

input = sys.stdin.readline

# 입력 받기
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# 카드에 있는 숫자들의 빈도 계산
card_counts = Counter(cards)

# 결과 출력
for n in nums:
    print(card_counts[n], end=' ')
