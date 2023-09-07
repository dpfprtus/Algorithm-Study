from sys import stdin,setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)

input = stdin.readline

def get_maxbranch(tree,root):
    if root not in tree: return 0

    maxbranch = 0
    for node,w in tree[root].items():
        del tree[node][root]
        branch = w + get_maxbranch(tree,node)
        if branch > maxbranch:
            maxbranch=branch
    return maxbranch

n,r = map(int,input().split())
tree = defaultdict(dict)
for i in range(n-1):
    a,b,d = map(int,input().split())
    tree[a][b] = d
    tree[b][a] = d

giganode = r
gigalen = 0

while len(tree[giganode]) == 1:
    node,w = list(tree[giganode].items())[0]
    del tree[node][giganode]
    gigalen += w
    giganode = node

maxbranch = get_maxbranch(tree,giganode)

print("{} {}".format(gigalen,maxbranch))
    
    