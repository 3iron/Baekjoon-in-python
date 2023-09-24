m = int(input())
n = int(input())
sumK = 0 # 소수의 합
minK = 0 # 소수의 최솟값
arr = []
answer = 0

# m 이상 n 이하의 자연수
for i in range(m, n+1):
    cnt = 0 
    
    for k in range(1, i+1):
        if (i%k==0):
            cnt += 1
            #print("i :", i, "나누기 k:", k)
    if(cnt == 2):
        sumK += k
        arr.append(i)
        minK = min(arr)

if (sumK == 0 and minK == 0):
    print(-1)
else:
    print(sumK)
    print(minK)