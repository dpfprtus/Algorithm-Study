n,k = map(int,input().split())
key = list(map(int,input().split()))
ans = []
for i in range(1,n):
    ans.append(key[i]-key[i-1])
ans.sort()
print(sum(ans[:n-k]))