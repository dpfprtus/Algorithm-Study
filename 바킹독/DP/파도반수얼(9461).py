t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0]*(n+1)
    
    if n == 1 or n == 2 or n == 3:
        print(1)
        continue
    elif n == 4 or n == 5:
        print(2)
        continue
    dp[1],dp[2],dp[3] = 1,1,1
    dp[4],dp[5] = 2,2

    for i in range(5,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])