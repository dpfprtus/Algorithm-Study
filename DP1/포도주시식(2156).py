n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[0] = s[0]
dp[1] = s[0]+s[1]
dp[2] = max(dp[0]+s[2],dp[1],s[1]+s[2])
for i in range(3,n):
    dp[i] = max(dp[i-2]+s[i],dp[i-1],s[i-1]+s[i]+dp[i-3])
print(dp)
print(dp[n-1])    