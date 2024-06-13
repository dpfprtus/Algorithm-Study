n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = [0]*m
isTrue2 = [0]*(10001)

def func(k):

    isTrue = [0]*(10001)

    if k == m:
        print(' '.join(map(str,ans)))
        return
    
    for i,value in enumerate(nums):
        if isTrue2[i] == 0:
            if isTrue[value] == 1 or(k !=0 and ans[k-1]>value):
                continue

            isTrue[value] = 1
            ans[k] = value
            isTrue2[i] = 1
            func(k+1)
            isTrue2[i] = 0
        
func(0)