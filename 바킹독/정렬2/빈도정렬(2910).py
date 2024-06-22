n,c = map(int,input().split())
nums = list(map(int,input().split()))

count = {}
idx = 1
for i in nums:
    if i in count:
        count[i][0] += 1
    else:
        count[i] = [1,idx]
        idx += 1

result = [[i,j] for i,j in count.items()]
result.sort(key=lambda x : (-x[1][0],x[1][1]))

res = []
for i,j in result:
    res += [i]*j[0]
print(*res)


