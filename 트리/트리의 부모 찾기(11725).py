from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
root = 1
parent = [[] for _ in range(n+1)]
q = deque()
visited = [False] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(tree,root):
    if not tree[root]: return
    visited[root] = True
    q.append(root)
    while q:
        node = q.popleft()
        for i in tree[node]:
            if not visited[i]:
                q.append(i)
                parent[i] = node
                visited[i] = True
bfs(tree,1)
print(*parent[2:],sep='\n')