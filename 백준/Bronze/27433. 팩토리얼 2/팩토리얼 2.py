# 0보다 크거나 같은 정수 N
# N! (팩토리얼) 출력 문제
# N = 0 이면 1 출력.

def factorial(N):
    if N == 0:
       return 1
    else:
        return N * factorial(N-1)
        
N = int(input())

print(factorial(N))
