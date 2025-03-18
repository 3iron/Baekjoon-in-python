

def solve():
    T = int(input()) # 테스트 케이스 개수
    for _ in range(T):
        num = input().split() 
        firstNum = float(num[0])
        for i in range(1, len(num)):
            if(num[i]=="@"):
              firstNum *= 3
            elif(num[i]=="%"):
              firstNum += 5
            elif(num[i]=="#"):
              firstNum -= 7
        print(f'{firstNum:.2f}')  # 계산 결과 소수점 둘째 자리까지 출력

solve()
    
