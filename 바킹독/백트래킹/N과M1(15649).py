n,m = map(int,input().split())

a = [0]*(n+1)
ans = [0]*m

def find(k):
    
    if k == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        if not a[i]:
            ans[k] = i
            a[i] = 1
            find(k+1)
            a[i] = 0
find(0)