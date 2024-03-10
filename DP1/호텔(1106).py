c,n = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]
dp = [1e9 for _ in range(c+100)]
dp[0] = 0
for cost,people in s:
    for i in range(people, c+100):
        dp[i] = min(dp[i-people]+cost,dp[i])

print(min(dp[c:]))
