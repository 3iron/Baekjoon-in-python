n = int(input())
arr = list(map(int, input().split()))
cnt = 0
t = 0

for i in range(0, len(arr)+1):
    # print(arr[i]) # 1 3 5 7
    for t in range(1, arr[i]+1):
        #if (arr[i]//t > 0):  # i = 0 일 때 , 1//1 > 0
        #    cnt += 1
        if (arr[i]%t == 0):
            print(arr[i], t)
            cnt +=1 
            # print(cnt)
        # print(cnt)
     
    
#    if (arr[i]//i == 1):
#        print(arr[i])


# i = 1 일 때, arr[1]//2 =
