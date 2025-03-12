nums = []
for _ in range(5):
    nums.append(int(input()))

# 평균
avg = sum(nums) // 5

# 중앙값
nums.sort()
med = nums[2]

print(avg)
print(med)