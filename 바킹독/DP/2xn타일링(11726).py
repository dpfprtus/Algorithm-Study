n = int(input())
dp = [0]*1001

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4,n+1):
    #오버플로가 발생할 수 있으니 계속 나머지 연산을 해줘야함.
    dp[i] = dp[i-1]+dp[i-2] % 10007
print(dp[n])