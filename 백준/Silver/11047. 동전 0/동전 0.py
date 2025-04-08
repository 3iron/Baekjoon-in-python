# 입력값
# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]

coins.reverse() # 큰 동전부터 사용하기 위해 내림차순

count = 0 
for coin in coins:
    if k==0:
        break
    count += k // coin # 해당 동전 사용 최대 개수
    k %= coin # 남은 금액 계산

print(count)
