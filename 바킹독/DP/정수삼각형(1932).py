n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*i for i in range(1,n+1)]

if n == 1:
    print(s[0][0])
elif n != 1 and n == 2:
    print(max(s[0][0]+s[1][0],s[0][0]+s[1][1]))
else:
    for idx,value in enumerate(s[-1]):
        dp[-1][idx] = value
    print(dp)
    for i in range(n-2,0,-1):
        for j in range(i+1):

            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + s[i][j]
        print(dp)
    print(max(dp[1][0]+s[0][0],dp[1][1]+s[0][0]))