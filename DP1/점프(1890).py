import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int,input().split())))
dp = [[0]* (n+1) for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break
        cur = m[i][j]
        if i+cur < n:
            dp[i+cur][j]+= dp[i][j]
        if j+cur < n:
            dp[i][j+cur] += dp[i][j]
