import sys
input = sys.stdin.readline

n = int(input())
dp = [1e9] * (5001)
dp[3] = 1
dp[5] = 1
s = [3,5]
for i in s:
    for j in range(i,n+1):
        dp[j] = min(dp[j-i]+1,dp[j])

if dp[n] == 1e9:
    print(-1)
else:
    print(dp[n])
