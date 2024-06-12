n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = [0]*m
isTrue = [0]*(10001)


def func(k):

    isTrue2 = [0]*(10001)

    if k == m:
        print(' '.join(map(str,ans)))
        return
    
    for i,value in enumerate(nums):
        if isTrue[i] == 0:
            if isTrue2[value] == 1:
                continue
            ans[k] = value
            isTrue[i] = 1
            isTrue2[value] = 1
            func(k+1)
            isTrue[i] = 0
        
func(0)