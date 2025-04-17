def solution(arr, n):
    answer = []
    # arr 배열 길이가 짝수면
    if (len(arr) % 2 == 0):
        # 홀수 번째 배열에만 n만큼 더한다
        for i in range(1, len(arr), 2):
            arr[i] += n
    else:
        # 짝수 번째 배열에만 n만큼 더한다
        for i in range(0, len(arr), 2): 
            arr[i] += n     
            
    
    answer = arr        
    return answer