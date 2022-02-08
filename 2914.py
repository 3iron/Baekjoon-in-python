a, i = map(int, input().split())
# 수록된 곡의 개수 a
# 평균값 i
# 구하려는것 = n : 적어도 몇 곡이 저작권이 있는 멜로디인지? 

# 저작권이 있는 멜로디의 개수 / 수록된 곡의 개수 (a)

# ex 38곡 수록, 저작권 멜로디 894 평균 23.53 올림 24

# 1. 올림하는방법
# 2. n / a = i
# n = 저작권이 있는 멜로디의 개수

# 1. round(실수, 소수점 n번째)
# 2. n = i * a

print(round((i-1)*a, 1))
