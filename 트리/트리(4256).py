def solve(preorder,inorder):
    if not preorder:return
    root = preorder[0]
    index = inorder.index(root)
    
    solve(preorder[1:index+1],inorder[:index])
    solve(preorder[index+1:],inorder[index+1:])
    print(root,end=' ')

for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    solve(preorder,inorder)
    print()

    
