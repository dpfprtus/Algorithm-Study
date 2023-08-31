k = int(input())
order = input().split()
tree = [[] for _ in range(k)]

def make(order,x):
    mid = len(order) // 2
    tree[x].append(order[mid])
    if len(order) == 1:
        return 
    make(order[:mid],x+1)
    make(order[mid+1:],x+1)
    
make(order,0)
for i in range(k):
    print(*tree[i])
