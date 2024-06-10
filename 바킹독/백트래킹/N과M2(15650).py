n,m = map(int,input().split())
ans = [0]*m
istrue = [0]*(n+1)

def func(k):

    if k == m:
        print(' '.join(map(str,ans)))
        return
    
    st = 1
    if k != 0:
        st = ans[k-1] + 1
    
    for i in range(st,n+1):
        if istrue[i] == 0:
            ans[k] = i
            istrue[i] = 1
            func(k+1)
            istrue[i] = 0
func(0)
