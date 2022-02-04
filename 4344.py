c = int(input())
avg = []

for i in range(c):
    n = list(map(int, input().split()))

    sum = 0
    for i in range(n[0]):
        sum += n[i + 1]