import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    n,k = map(int,input().split())
    if n == 0 and k == 0:
        break
    num = list(map(int,input().split()))
    parent = defaultdict(int)
    index = 0
    for i in range(1,n):
        parent[num[i]] = num[index]
        if i < n-1 and num[i+1]-num[i] != 1:
            index += 1
    cnt = 0
    for i in num:
        if parent[parent[k]] and parent[parent[k]] == parent[parent[i]] and parent[k] != parent[i]:
           cnt += 1 
    print(cnt)
            
