t = int(input())

#0출력횟수, 1출력횟수
dp = [[0]*41 for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 0
dp[1][1] = 1

for i in range(2,41):
    dp[i][0] = dp[i-1][0]+dp[i-2][0]
    dp[i][1] = dp[i-1][1]+dp[i-2][1]

for _ in range(t):
    n = int(input())
    print(dp[n][0],dp[n][1])