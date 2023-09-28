from sys import setrecursionlimit
setrecursionlimit(10**9)

n = int(input())
parent = list(map(int,input().split()))
erase = int(input())

def dfs(root):
    parent[root] = -2
    for i in range(len(parent)):
        if parent[i] == root:
            dfs(i)

dfs(erase)
count = 0
for i in range(len(parent)):
    if parent[i] != -2 and i not in parent:
        count += 1
print(count)