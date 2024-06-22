n = int(input())
nums = [input().rstrip() for _ in range(n)]
nums = list(set(nums))
nums.sort()
nums.sort(key=lambda x : len(x))

for i in nums:
    print(i)