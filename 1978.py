n = int(input())
arr = list(map(int, input().split()))
a = 0
answer = 0

for i in range(0, n): 
    a = arr[i]
    cnt = 0

    for _ in range(1, a+1):
        if(a%_==0):        
            cnt += 1 
    if (cnt == 2):
        answer += 1
    

print(answer)