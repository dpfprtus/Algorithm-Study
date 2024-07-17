from bisect import bisect_left

n = int(input())
nums = list(map(int,input().split()))
nums2 = list(set(nums))
nums2.sort()

for num in nums:
    print(bisect_left(nums2,num),end=" ")
    