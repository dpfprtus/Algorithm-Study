n = int(input())
stair = [0]+[int(input()) for _ in range(n)]

dp = [0]*301

if n == 1:
    print(stair[1])
elif n == 2:
    print(stair[2]+stair[1])
elif n == 3:
    print(max(stair[1]+stair[3],stair[2]+stair[3]))
else:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[1]+stair[3],stair[2]+stair[3])
    for i in range(4,n+1):
        dp[i] = max(dp[i-2]+stair[i],stair[i]+stair[i-1]+dp[i-3])

    print(dp[n])