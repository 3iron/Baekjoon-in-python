a, b, c = map(int, input().split())
c = c + int(input())
b = b + int(c//60)
a = a + int(b//60)
a = a % 24
b = b % 60
c = c % 60
print(a, b, c)