from collections import defaultdict

n = int(input())

tree = defaultdict(str)

def pre_order(node):
    b,c = tree[node]
    
    print(node,end='')
    if b != ".":
        pre_order(b)
    if c != ".":
        pre_order(c)

def in_order(node):
    b,c = tree[node]
    if b != ".":
        in_order(b)
    print(node,end='')
    if c != ".":
        in_order(c)

def post_order(node):
    b,c = tree[node]
    if b != ".":
        post_order(b)
    if c != ".":
        post_order(c)
    print(node, end='')

for i in range(n):
    a,b,c = input().split()
    tree[a] = (b,c)

pre_order('A')
print()
in_order('A')
print()
post_order('A')
    
