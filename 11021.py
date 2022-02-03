n = int(input())

for i in range(1,n+1):
    a,b = map(int, input().split())
    r = a+b
    print("Case #"+str(i)+':',r)