from collections import deque

def bfs():
    q = deque([])
    while True:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            if maps[x][y] == 0 and maps[nx][ny] != 0:
                maps[nx][ny] -= 1
            visit[nx][ny] = 1
            q.append((nx,ny))

n,m = map(int,input().split())
maps = [list(map(int,input().split(' '))) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
