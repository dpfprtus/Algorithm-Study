import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
maps = []
virus = []

for i in range(n):
    a = list(map(int,input().split()))
    maps.append(a)
    for j in range(m):
        if a[j] == 2:
            virus.append((i,j))

stack = [[0,0],[0,0],[0,0]]
visited = [[0]*m for _ in range(n)]
result = 0

def count_map(tmp):
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    return count

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(tmp,stack):

    for x,y in stack:
        tmp[x][y] = 1
    q = deque(virus)
    visited = [[0]*m for _ in range(n)]
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0 and tmp[nx][ny] != 2 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                tmp[nx][ny] = 2
                q.append((nx,ny))
    return tmp
                
def dfs(x):
    global result
    if x == 3:
        tmp = [[j for j in maps[i]] for i in range(n)]
        tmp = bfs(tmp,stack)
        result = max(result,count_map(tmp))
        return
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0 and visited[i][j] == 0:
                stack[x] = [i,j]
                visited[i][j] = 1
                dfs(x+1)
                visited[i][j] = 0
dfs(0)
print(result)