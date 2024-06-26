n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

result = 0
count = 1

if len(nums) == 1:
    print(nums[0])
    exit()
for i in range(len(nums)):
    if nums[i-1] == nums[i]:
        count += 1
    else:
        if result < count:
            max_idx = nums[i-1]
        result = max(count,result)
        count = 1

    
print(max_idx)
    