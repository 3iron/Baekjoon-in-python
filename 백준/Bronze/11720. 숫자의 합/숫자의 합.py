n = int(input()) # 숫자의 개수
# nums = map(int, input().split()) # 띄어쓰기 공백이 있어야 split 가능
nums = input()
sum = 0

for i in range(n):
    sum += int(nums[i])

print(sum)
