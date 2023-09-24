from collections import defaultdict

def preOrder(node):
    b,c = tree[node]

    print(node,end='')
    if b != ".":
        preOrder(b)
    if c != ".":
        preOrder(c)
        
def inOrder(node):
    b,c = tree[node]
    if b!= ".":
        inOrder(b)
    print(node,end='')
    if c!= ".":
        inOrder(c)

def postOrder(node):
    b,c = tree[node]
    if b!= ".":
        postOrder(b)
    if c!= ".":
        postOrder(c)
    print(node,end='')

n = int(input())
tree = defaultdict(str)
for i in range(n):
    a,b,c = input().split()
    tree[a] = (b,c)
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')