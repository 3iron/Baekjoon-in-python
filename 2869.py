a, b, v = map(int,input().split())
# a 미터 올라가고 b 만큼 내려가고 
# v 높이를 올라가야 함

i = 0 # 몇 번 실행됐는지
n = 0 # 현재 위치

while True:
    i += 1
    n += a
    n -= b
    if(n>=v):
        print(i)
        break
    
        
        
