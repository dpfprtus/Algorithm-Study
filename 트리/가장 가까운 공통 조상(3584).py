from sys import setrecursionlimit
setrecursionlimit(10**9)

def dfs(tree,a):
    for node in tree[a]:
        if visited[node] == False:
            result.append(node)
            dfs(tree,node)

for _ in range(int(input())):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for i in range(n-1):
        a,b = map(int,input().split())
        tree[b].append(a)
    node1,node2 = map(int,input().split())
    visited = [False] * (n+1)
    visited[node1] = True
    result = [node1]
    dfs(tree,node1)

    visited = [False] * (n+1)
    visited[node2] = True
    result1 = result
    result = [node2]
    dfs(tree,node2)
    flag = 0
    for i in result:
        for j in result1:
            if i == j:
                print(i)
                flag = 1
                break
        if flag == 1:
            break
            




