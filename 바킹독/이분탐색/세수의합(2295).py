from bisect import bisect_left

n = int(input())
nums = [int(input()) for _ in range(n)] 
nums.sort()

nums_two = []

for i in range(n):
    for j in range(i,n):
        nums_two.append((nums[i]+nums[j]))
nums_two.sort()

for i in range(len(nums)-1,-1,-1):
    for j in range(i):
        idx = bisect_left(nums_two,nums[i]-nums[j])
        if nums_two[idx] == nums[i]-nums[j]:
            print(nums[i])
            exit()
