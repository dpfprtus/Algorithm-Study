n = int(input())

dp = [0]*1000001

result = [0]*(n+1)
for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    result[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3]+1
        result[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
        result[i] = i//2
        
print(dp[n])
cur = n
while True:

    if cur == 0:
        break
    print(cur,end=" ")
    cur = result[cur]