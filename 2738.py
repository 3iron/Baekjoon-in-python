N, M = map(int, input().split())
A = []
B = []

# 행렬 A 입력
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 덧셈 및 출력
for i in range(N):
    result_row = []
    for j in range(M):
        result_row.append(A[i][j] + B[i][j])
    print(*result_row)