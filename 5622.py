a = input().lower()
answer = 0

dial = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

# 3, 4, 5, 6, 7, 8, 9, 10

for i in range(len(dial)):       # len(dial) = 8, i=0 일 때 dial[0]은 'abc'
    p = dial[i]
    r = 0
    for j in range(len(p)):      # len(p) = 3,  j=0 일 때 p[0:1] 은 a
        r = r + 1
        # print(p[j:r])
        
        if a == p[j:r] :
            # print(p[j:r])
            # print(j)
            # print(r)
            print(i+2)
            # answer = i+1
            
        
        
        # if a == p[j:r] :
        #     answer = a
        # else :
        #     r += 1    

# print (answer)
# print(len(dial))
# print(p)
# print(a)