n = int(input())
tree = [[] for _ in range(n+1) ] 
visited = [False] * (n+1)

def dfs(tree,v,visited):
    for i in tree[v]:
        if not visited[i]:
            visited[i] = v
            dfs(tree,i,visited)

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(tree,1,visited)

for i in range(2,n+1):
    print(visited[i])
