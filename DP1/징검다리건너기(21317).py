n = int(input())
energy = [list(map(int,input().split())) for _ in range(n-1)]
k = int(input())
dp = [0]*n
if n == 1:
    print(0)
    exit()
elif n == 2:
    print(energy[0][0])
    exit()
    
dp[1] = energy[0][0]
dp[2] = min(dp[1]+energy[1][0],energy[0][1])

for i in range(3,n):
    dp[i] = min(dp[i-1]+energy[i-1][0],energy[i-2][1]+dp[i-2])

res = dp[-1]
dp2 = dp[:]
for i in range(n-3):
    if dp[i] + k < dp[i+3]:
        dp2[i+3] = dp[i]+k
        for j in range(i+4,n):
            dp2[j] = min(dp[j],dp2[j-1]+energy[j-1][0], energy[j-2][1]+dp2[j-2])
        if dp2[-1] < res:
            res = dp2[-1]
print(res)
    