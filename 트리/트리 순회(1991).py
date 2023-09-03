n = int(input())
tree = {}

def preorder(root):
    if root != ".":
        print(root,end= '')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def middleorder(root):
    if root != ".":
        middleorder(tree[root][0])
        print(root,end='')
        middleorder(tree[root][1])
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

for _ in range(n):
    a,b,c = input().split()
    tree[a] = [b,c]
    
preorder("A")   
print()
middleorder("A")
print()
postorder("A")