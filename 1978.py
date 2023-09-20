n = int(input())
arr = list(map(int, input().split()))
t = 0
# answer = 0


for i in range(0, len(arr)+1):
    cnt = 0
    for t in range(1, arr[i]+1):
        if (arr[i]%t == 0):
            # print(arr[i], t) # i=0, t = 1 -> 1, 1.  // i=1, t=1, t=3 
            cnt +=1
        if cnt == 2:
            print(arr[i], " 가 소수에요")
            # answer += 1

# print(answer)
        
