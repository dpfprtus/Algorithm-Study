from sys import setrecursionlimit
setrecursionlimit(10 ** 9)
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int,input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))

a = [0]
def dfs(node,we):
    for node,w in tree[node]:
        if distance[node] == -1:
            distance[node] = we+w
            dfs(node,we+w)
            
distance = [-1] * (n+1)
distance[1] = 0

result = dfs(1,0)
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
result2 = dfs(start,0)
print(max(distance))