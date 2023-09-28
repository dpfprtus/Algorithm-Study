def makePost(preorder,inorder):
    if not preorder: return
    root = preorder[0]
    index = inorder.index(root)
    makePost(preorder[1:index+1],inorder[:index+1])
    makePost(preorder[index+1:],inorder[index+1:])
    print(root,end=' ')

t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    makePost(preorder,inorder)
    print()