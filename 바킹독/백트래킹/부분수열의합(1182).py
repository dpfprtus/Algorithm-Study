n,s = map(int,input().split())
nums = list(map(int,input().split()))

def func(idx,ans):
    global cnt
    if idx >= n:
        return
    
    
    ans += nums[idx]
    if ans == s:
        cnt += 1 

    func(idx+1,ans)
    func(idx+1,ans-nums[idx])
    
cnt = 0
func(0,0)
print(cnt)