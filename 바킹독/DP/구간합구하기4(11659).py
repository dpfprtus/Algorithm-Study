import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    nums[i] = nums[i-1]+nums[i]
for _ in range(m):
    i,j = map(int,input().split())
    print(nums[j]-nums[i-1])

    