a, b = map(int, input().split())

if b-45 >= 0:
    print(a, b-45)
elif a>0 and b-45 < 0:
    print(a-1,60+b-45)
else :
    print(23, 60+b-45)
