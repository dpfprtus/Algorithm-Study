from itertools import combinations

n,k = map(int,input().split())
height = list(map(int,input().split()))
price = 0
ans = []
for i in range(1,n):
    ans.append(height[i]-height[i-1])
print(ans)
ans.sort(reverse=True)
print(ans)
print(sum(ans[k-1:]))


