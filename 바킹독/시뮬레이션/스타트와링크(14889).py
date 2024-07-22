from itertools import combinations

n = int(input())
nums = [i for i in range(1,n+1)]
maps = [list(map(int,input().split())) for _ in range(n)]

def cal(tmp1,tmp2):
    result1 = 0
    result2 = 0
    for x,y in combinations(tmp1,2):
        result1 += maps[x-1][y-1] + maps[y-1][x-1]
    for x,y in combinations(tmp2,2):
        result2 += maps[x-1][y-1] + maps[y-1][x-1]
    return abs(result1 - result2)

result = float("inf")
a = [0]*(int(n/2))
visited = [0]*(n+1)

def dfs(x,idx):
    visited2 = [0]*(n+1)
    global result
    if x == (n//2):
        
        b = [i for i in nums if i not in a]
        result = min(result,cal(a,b))
        return

    for i in range(idx,n+1):
        if visited[i] == 0:
            a[x] = i
            visited[i] = 1
            visited2[i] = 1
            dfs(x+1,i+1)
            visited[i] = 0
dfs(0,1)
print(result)
#n은 짝수