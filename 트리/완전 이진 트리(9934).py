import sys
input = sys.stdin.readline

k = int(input())
order = list(map(int,input().split()))
tree = [[] for _ in range(len(order))]
def search(order,x):
    
    root = len(order) // 2
    tree[x].append(order[root])
    if len(order) == 1: return
    search(order[:root],x+1)
    search(order[root+1:],x+1)
    
search(order,0)
for i in tree:
    if i:
        print(*i)
