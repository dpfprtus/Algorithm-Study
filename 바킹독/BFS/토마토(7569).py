from collections import deque

m,n,h = map(int,input().split())
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
maps = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

q = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 1:
                q.append((j,k,i))

while q:
    x,y,z = q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and visit[nz][nx][ny] == 0 and maps[nz][nx][ny] == 0:
            visit[nz][nx][ny] = visit[z][x][y] + 1
            maps[nz][nx][ny] = 1
            q.append((nx,ny,nz))

time = 0
flag = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 0:
                flag = 1
                break
            else:
                time = max(time,visit[i][j][k])
                
if flag:
    print(-1)
else:
    print(time)