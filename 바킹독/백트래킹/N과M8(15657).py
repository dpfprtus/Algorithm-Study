n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = [0]*m

def func(k):
    
    if k == m:
        print(' '.join(map(str,ans)))
        return

    for i in nums:
        if k!=0 and ans[k-1] > i:
            continue
        ans[k] = i
        func(k+1)
        
func(0)