import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int,input().split())))
dp = [[0]*(n+1) for _ in range(n)]
dp[0][0] =1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        if dp[i][j] != 0 and i + s[i][j]< n:
            dp[i+s[i][j]][j] += dp[i][j]
        if dp[i][j] != 0 and j + s[i][j]< n:
            dp[i][j+s[i][j]] += dp[i][j]
print(dp)
print(dp[n-1][n-1])
