import sys
input = sys.stdin.readline

n = int(input())
point = [0]+[int(input()) for _ in range(n)]

dp = [0] * (n+1)
if n == 1:
    print(point[1])
    exit()
elif n == 2:
    print(point[1] + point[2])
    exit()
elif n == 3:
    print(max(point[1]+point[3], point[2]+point[3]))
    exit()
dp[1] = point[1]
dp[2] = point[1] + point[2]
dp[3] = max(point[1]+point[3], point[2]+point[3])
for i in range(4,n+1):
    dp[i] = max(point[i]+dp[i-2],point[i]+point[i-1]+dp[i-3])
print(dp[n])