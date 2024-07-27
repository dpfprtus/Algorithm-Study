
n = int(input())
tree = [[] for _ in range(n+1)]
parent = [[0] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(cur):
    for nxt in tree[cur]:
        if parent[cur] == nxt:
            continue
        parent[nxt] = cur
        dfs(nxt)
dfs(1)
for i in range(2,n+1):
    print(parent[i])