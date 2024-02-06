n,k = map(int,input().split())
s = list(map(int,input().split()))

dp = [0]*n
dp[0] = 1
for i in range(n-1):
    if dp[i] == 1:
        for j in range(1,n):
            if dp[j] == 0 and (j-i) * (1+abs(s[i]-s[j])) <= k:
                dp[j] = 1
print("YES" if dp[n-1] else "NO") 