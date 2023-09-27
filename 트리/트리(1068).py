from sys import setrecursionlimit
setrecursionlimit(10**9)

n = int(input())
parent = list(map(int,input().split()))
remove_node = int(input())
tree = [[] for _ in range(n+1)]

def delNode(node):
    for i in tree[node]:
        delNode(i)
        tree[i] = 0

for i in range(1,n):
    tree[parent[i]].append(i)
    tree[i].append(parent[i])
print(tree)
delNode(remove_node)
tree[remove_node] = 0
