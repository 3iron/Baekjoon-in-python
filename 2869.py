# a, b, v = map(int,input().split())
# # a 미터 올라가고 b 만큼 내려가고 
# # v 높이를 올라가야 함

# i = 0 # 몇 번 실행됐는지
# n = 0 # 현재 위치

# while True:
#     i += 1
#     n += a
#     n -= b
#     if(n>=v):
#         print(i)
#         break

# -> 런타임 에러로 다른 사람 풀이 참고

import math

a, b, v = map(int, input().split())
day = (v-b) / (a-b)
print(math.ceil(day))

# math.ceil 함수 -> 숫자를 반올림함
# 풀이에서 배운것 : 거꾸로 생각하기. 결과부터 생각하면 됨.
        
        
