import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = []
num = []
for i in range(n):
    s.append(list(map(int,input().split())))

for i in range(m):
    num.append(list(map(int,input().split())))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j] +dp[i][j-1]+s[i-1][j-1]-dp[i-1][j-1]

for i in num:
    a,b,c,d = i
    print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])
