n = int(input())
nums = list(map(int,input().split()))

dp = [1]*(n)
dp[0] = nums[0]

for i in range(1,n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i],dp[j]+nums[i])
        else:
            dp[i] = max(dp[i],nums[i])

print(max(dp))