n,m = map(int,input().split())
ans = [0]*m

def func(k):
    if k == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(1,n+1):
        ans[k] = i
        if (k != 0 and ans[k-1] > i):
            continue
        func(k+1)
func(0)