import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
nodeNum = [0] * (n+1)
for i in range(n):
    nodeNum[inorder[i]] = i

def makePreorder(instart,inend,poststart,postend):
    if instart > inend or poststart > postend: return
    root = postorder[postend]
    leftnode = nodeNum[root] - instart
    rightnode = inend - nodeNum[root]
    print(root,end= " ")
    makePreorder(instart,instart+leftnode-1,poststart,poststart+leftnode-1)
    makePreorder(inend-rightnode+1,inend,postend-rightnode,postend-1)

makePreorder(0,n-1,0,n-1)