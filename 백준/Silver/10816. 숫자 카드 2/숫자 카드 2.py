import sys
from collections import Counter

# 빠른 입력
input = sys.stdin.readline

# 입력
N = int(input())  # 숫자 카드 개수
cards = list(map(int, input().split())) # 숫자 카드에 적힌 정수 N개
M = int(input()) # 확인할 숫자 개수 M
targets = list(map(int, input().split())) # 확인할 숫자들

# 카드 개수 세기
card_counter = Counter(cards)

# 출력
result = [str(card_counter[target]) for target in targets]
print(' '.join(result))