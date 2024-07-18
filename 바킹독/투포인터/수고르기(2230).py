n,m = map(int,input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
a = float("inf")
st,en = 0,0
for i in range(2*n):
    if en > n-1 or st > n-1:
        break
    if nums[en]-nums[st] >= m:
        a = min(a,nums[en]-nums[st])
        st += 1
    else:
        en += 1
print(a)
        