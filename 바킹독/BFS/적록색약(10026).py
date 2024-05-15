from collections import deque

n = int(input())
maps = [input() for _ in range(n)]
visit = [[0]*101 for _ in range(101)]

dx = [0,1,-1,0]
dy = [1,0,0,-1]

count = 0
count2 = 0

def bfs(x,y):
    q = deque([(x,y)])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and maps[x][y] == maps[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx,ny))

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            count += 1

for i in range(n):
    maps[i] = maps[i].replace("R","G")
    
visit = [[0]*101 for _ in range(101)]

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j)
            count2 += 1

print(count,count2)
