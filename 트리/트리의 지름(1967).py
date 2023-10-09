from sys import setrecursionlimit
setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child,w = map(int,input().split())
    tree[parent].append([child,w])
    tree[child].append([parent,w])

def dfs(node,we):
    for i in tree[node]:
        a,b = i
        if distance[a] == -1:
            distance[a] =  we+b
            dfs(a,we+b)


distance = [-1] * (n+1)
distance[1] = 0
dfs(1,0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start,0)
print(max(distance))