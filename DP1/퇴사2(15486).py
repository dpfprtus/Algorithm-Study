import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    t,p = map(int,input().split())
    dp[i] = max(dp[i],dp[i-1])
    if t+i <= n+1:
        dp[t+i-1] = max(dp[t+i-1],dp[i-1]+p)
print(dp[-1])