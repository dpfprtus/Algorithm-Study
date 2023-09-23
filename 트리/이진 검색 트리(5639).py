import sys
from sys import setrecursionlimit
setrecursionlimit(10**9)
input = sys.stdin.readline
tree = []

def post(start,end):
    if start > end: return
    mid = end+1
    for i in range(start+1,end+1):
        if tree[i] > tree[start]:
            mid = i
            break
    post(start+1,mid-1)
    post(mid,end)
    print(tree[start])
    

while True:
    try:
        tree.append(int(input()))
    except:
        break
post(0,len(tree)-1)
