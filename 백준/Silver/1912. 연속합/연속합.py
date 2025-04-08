# 입력값
# 10
# 10 -4 3 1 5 6 -35 12 21 -1

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n # dp 배열 초기화
dp[0] = arr[0] # 첫 수는 그대로 시작
max_sum = dp[0] # 결과값 초초기화

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i]) # 누적 합의 최대와 비교
    max_sum = max(max_sum, dp[i]) # 최대값 갱신

print(max_sum)