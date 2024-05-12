n,m = map(int,input().split())
maps = [input() for _ in range(n)]
dist = [[-1]*101 for _ in range(101)]


dx = [-1,0,1,0]
dy = [0,-1,0,1]
q = [(0,0)]

while q:
    x,y = q.pop(0)
    if dist[x][y] == -1:
        dist[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if dist[nx][ny] != -1 or int(maps[nx][ny]) == 0:
            continue
        q.append((nx,ny))
        dist[nx][ny] = dist[x][y] + 1
print(dist[n-1][m-1]) 