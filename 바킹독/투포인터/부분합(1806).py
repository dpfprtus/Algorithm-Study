
n,s = map(int,input().split())
nums = list(map(int,input().split()))

a = float("inf")

st,en = 0,0
total = nums[0]
for st in range(n):
    while en < n and total < s:
        en += 1
        if en != n:
            total += nums[en]
    if en == n:
        break
    a = min(a,en-st+1)
    total -= nums[st]
        

if a == float("inf"):
    print(0)
else:
    print(a)