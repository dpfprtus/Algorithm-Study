import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)




q = int(input())
for i in range(q):
    t,k = map(int,input().split())
    if t == 1:
        if len(tree[k]) < 2:
            print("no")
        else:
            print("yes")
    elif t == 2:
        print("yes")

