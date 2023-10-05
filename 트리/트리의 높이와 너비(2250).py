n = int(input())
row = [list() for _ in range(n+1)]
tree = [[0,0] for _ in range(n+1)]
root = [0] * (n+1)
col = 1

def findRoot():
    return root.index(1)

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
    root[node] += 1
    if left != -1: root[left]+=1
    if right != -1: root[right] +=1 
dfs(findRoot(),1)
max_length = max(row[1])-min(row[1])+1
index = 0
for i in range(2,len(row)):
    if not row[i]:break
    length = max(row[i])-min(row[i])+1
    if length > max_length:
        max_length = length
        index = i
print(index,max_length)
