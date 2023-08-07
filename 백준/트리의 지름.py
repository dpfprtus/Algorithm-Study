n = int(input())

graph = [[0]*n]
result = -1e9
for i in range(n):
    a,b,c = map(int,input().split())
    graph[i].append((b,c))
def dfs():
    