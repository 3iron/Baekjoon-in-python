
# Online Python - IDE, Editor, Compiler, Interpreter

# N개의 물건
# 각 무게 W와 가치 V를 가진다.
# 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
# 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하라.

# 동적 프로그래밍 (DP)

# 첫 줄은 N(물건 개수),K(버틸 수 있는 무게)
N, K = map(int, input().split())

# 예시 데이터 
# 4 7 
# 6 13
# 4 8
# 3 6
# 5 12

# items : 2차원 리스트, W(무게),V(가치)를 저장
items = [[0,0]]

# 첫 줄의 N이 4이므로 4개 라인 range()로 input 값을 넣어준다
for _ in range(N):
    items.append(list(map(int, input().split())))

# items : 
# print(items)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = items[i][0]
        value = items[i][1]
        
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])


