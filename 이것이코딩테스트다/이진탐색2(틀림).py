n,m = list(map(int,input().split()))
dduck = list(map(int,input().split()))
dduck.sort()
result = 0
start = 0
end = max(dduck)

while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in dduck:
        if i > mid:
            total += i - mid
        
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)