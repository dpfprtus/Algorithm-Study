n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = [0]*m
istrue = [0]*(10001)

def func(k):
    
    if k == m:
        print(' '.join(map(str,ans)))
        return

    for i in nums:
        ans[k] = i
        func(k+1)
        
func(0)