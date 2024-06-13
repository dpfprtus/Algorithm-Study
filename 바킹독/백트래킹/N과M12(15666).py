n,m = map(int,input().split())
nums = list(map(int,input().split()))

nums = set(nums)
nums = list(nums)
nums.sort()
ans = [0]*m

def func(k):

    if k == m:
        print(' '.join(map(str,ans)))
        return
    
    for value in nums:
        if k != 0 and ans[k-1] > value:
            continue
        ans[k] = value
        func(k+1)
  
func(0)