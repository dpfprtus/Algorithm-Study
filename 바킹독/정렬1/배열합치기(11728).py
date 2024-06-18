n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = []

a_idx = 0
b_idx = 0
for i in range(n+m):
    if a_idx > n-1:
        result.append(b[b_idx])
        b_idx += 1
        continue
    if b_idx > m-1:
        result.append(a[a_idx])
        a_idx += 1
        continue
         
    elif a[a_idx] <= b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1
    else:
        result.append(b[b_idx])
        b_idx+=1
print(*result)
    

    
