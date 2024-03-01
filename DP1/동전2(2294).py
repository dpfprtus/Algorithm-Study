n,k = map(int,input().split())
values = [int(input()) for _ in range(n)]
dp = [10001]*(k+1)
dp[0] = 0
for value in values:
    for j in range(value,k+1):
        if dp[j] > 0:
            dp[j] = min(dp[j-value]+1,dp[j])
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])