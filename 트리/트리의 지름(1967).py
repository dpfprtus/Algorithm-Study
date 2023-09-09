n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,w = map(int,input().split())
    tree[a].append((b,w))

def getmax(tree,root):

    maxbranch = 0

    node,w = root
    branch = w + getmax(tree,node)
    if branch > maxbranch:
        maxbranch = branch
    return maxbranch

root = 1
result = []
print(tree[root][0])
while len(tree[root]) != 0 and root < len(tree):

    a = getmax(tree,tree[root][0])
    b = getmax(tree,tree[root][1])
    result.append(a+b)
    root += 1

print(max(result))