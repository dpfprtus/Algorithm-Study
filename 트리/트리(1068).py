n = int(input())
parent = list(map(int,input().split()))
erase = int(input())
cnt = 0
def dfs(root):
    parent[root] = -2
    for i in range(n):
        if parent[i] == root:
            dfs(i)
dfs(erase)
for i in range(n):
    if parent[i] != -2 and i not in parent:
            cnt += 1
          

print(cnt)