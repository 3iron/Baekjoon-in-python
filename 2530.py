a, b, c = map(int, input().split())
d = int(input())

if(d//60>0):
    b += d//60
    c += (d - d//60 * 60)

if (c//60>0):
    b += (c//60)
    c -= (c//60) * 60

if (b//60>0):
    a += (b//60)
    b -= (b//60) * 60
    
if (a//24>0):
    a -= (a//24) * 24 
    
print(a, b, c)



