n = int(input())
tree = [[0,0] for _ in range(n+1)]
row = [list() for _ in range(n+1)]
root_check = [0] * (n+1)
col = 1

def find_root():
    return root_check.index(1)

def dfs(node,level):
    global col
    left,right = tree[node]
    if tree[node][0] != -1:
        dfs(left,level+1)
    row[level].append(col)
    col += 1
    if tree[node][1] != -1:
        dfs(right,level+1)


for _ in range(n):
    node,left,right = map(int,input().split()) 
    tree[node] = [left,right]
    root_check[node] += 1
    if left != -1:root_check[left] += 1
    if right != -1:root_check[right] += 1

dfs(find_root(),1)

level = 1
max_dist = max(row[1])-min(row[1])+1
for i in range(2,n+1):
    if not row[i]: break
    distance = max(row[i])-min(row[i])+1
    if max_dist < distance:
        max_dist = distance
        level = i

print(level,max_dist)
