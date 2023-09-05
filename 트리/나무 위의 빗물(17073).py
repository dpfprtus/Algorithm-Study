#확률: w를 말단 노드 갯수로 나눈다. => 시간이 흐르면 말단노드에만 물이 고여있기 때문
from sys import stdin
from collections import defaultdict
input = stdin.readline
degree = defaultdict(int)
n,w = map(int,input().split())

for _ in range(n-1):
    u,v = map(int,input().split())
    degree[u] += 1
    degree[v] += 1
cnt = 0
for i in range(2,n+1):
    if degree[i] == 1:
        cnt += 1

print(w/cnt)



