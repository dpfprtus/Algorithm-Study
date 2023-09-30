from sys import setrecursionlimit,stdin
from collections import defaultdict
setrecursionlimit(10**9)
input = stdin.readline
        
def findMaxLength(tree,node):
    if node not in tree:return
    max_length = 0
    for b,d in tree[node].items():
        del tree[b][node]
        length = findMaxLength(tree,b)+d
        if length > max_length:
            max_length = length
    return max_length

n,r = map(int,input().split())
tree = defaultdict(dict)

for _ in range(n-1):
    a,b,d = map(int,input().split())
    tree[a][b] = d
    tree[b][a] = d
    
giga_length = 0
giga = r
while (len(tree[giga]) == 1):
    node,w = list(tree[giga].items())[0]
    del tree[node][giga]
    giga_length += w
    giga = node
maxbranch = findMaxLength(tree,giga)
print("{} {}".format(giga_length,maxbranch))

    