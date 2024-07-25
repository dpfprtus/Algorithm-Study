n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(n+1)
result = 0
def dfs(x):
    
    if visited[x] == 1:
        return
    
    visited[x] = 1
    for i in graph[x]:
        dfs(i)

for i in range(1,n+1):
    
    if visited[i] == 1:
        continue

    dfs(i)
    result += 1

print(result)
