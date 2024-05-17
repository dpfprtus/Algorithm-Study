from collections import deque

def bfs():
    q = deque([(0,0,0)])

    while q:
        x,y,count = q.popleft()
        if (x,y) == (n-1,m-1):
            return visit[x][y][count]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "1" and count == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    q.append((nx,ny,1))
                elif maps[nx][ny] == "0" and visit[nx][ny][count] == 0:
                    visit[nx][ny][count] = visit[x][y][count] + 1
                    q.append((nx,ny,count))
      
    return -1

n,m = map(int,input().split())
maps = [input() for _ in range(n)]
visit = [[[0,0] for _ in range(m)] for _ in range(n)]

visit[0][0][0] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

print(bfs())




