n = int(input())
s = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

s.sort()

def binarysort(x):
    st = 0
    en = n-1
    
    while st <= en:
        mid = (st+en) // 2
        if s[mid] > x:
            en = mid-1
        elif s[mid] < x:
            st = mid+1
        else:
            return True
    return False

for i in nums:
    if binarysort(i):
        print(1)
    else:
        print(0)