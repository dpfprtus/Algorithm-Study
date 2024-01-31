import sys
input = sys.stdin.readline
n = int(input())
s = [int(input()) for _ in range(n)]
if n == 1:
    print(s[0])
    
elif n == 2:
    print(s[0]+s[1])
elif n == 3:
    dp=[0]*10000
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    print(max(dp[0]+s[2],dp[1],s[1]+s[2]))
else:
    dp=[0]*10000
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    dp[2] = max(dp[0]+s[2],dp[1],s[1]+s[2])
    for i in range(3,n):
        dp[i] = max(dp[i-2]+s[i],dp[i-1],s[i-1]+s[i]+dp[i-3])

    print(max(dp))    