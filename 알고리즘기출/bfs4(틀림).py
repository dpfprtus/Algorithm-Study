n = int(input())
number = list(map(int,input().split()))
plus,minus,multiple,divide = map(int,input().split())

min_result = 1e9
max_result = -1e9

def dfs(i,now):
    global min_result,max_result,plus,minus,multiple,divide
    if i == n:
        min_result = min(min_result,now)
        max_result = max(max_result,now)
    else:   
        if plus > 0:
            plus -= 1
            dfs(i+1,now+number[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1,now-number[i])
            minus += 1
        if multiple > 0:
            multiple -= 1
            dfs(i+1,now*number[i])
            multiple += 1
        if divide > 0:
            divide -= 1
            dfs(i+1,int(now/number[i]))
            divide += 1
dfs(1,number[0])
print(max_result)
print(min_result)