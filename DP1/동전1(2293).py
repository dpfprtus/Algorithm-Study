n,k = map(int,input().split())

values = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1
for i in values:
    for j in range(i,k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])