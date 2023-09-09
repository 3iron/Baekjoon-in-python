import sys
input = sys.stdin.readline # 출력 속도를 빠르게 해준다

n, m = map(int, input().split())
A = [[0] * (n+1)]  # 1차원 배열
D = [[0]*(n+1) for _ in range(n+1)] # 2차원 배배열

for i in range(n):  # 원본 배열 받는
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]