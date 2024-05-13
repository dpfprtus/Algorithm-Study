from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
maps = [input() for _ in range(r)]
visit = [[0]*1001 for _ in range(1001)]
visit2 = [[0]*1001 for _ in range(1001)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
fire = deque([])
ji = deque([])

for i in range(r):
    for j in range(c):
        if maps[i][j] == "J":
            ji.append((i,j))
        elif maps[i][j] == "F":
            fire.append((i,j))

def bfs():
    while fire:
        a,b = fire.popleft()

        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na < 0 or na >= r or nb < 0 or nb >= c:
                continue
            if maps[na][nb] == "#" or visit[na][nb] >= 1:
                continue
            visit[na][nb] = visit[a][b] + 1
            fire.append((na,nb))
    while ji:
        x,y = ji.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return visit2[x][y]+1         
            if maps[nx][ny] == "#" or visit2[nx][ny] >= 1:
                continue
            if maps[nx][ny] == "F" or visit[nx][ny] > 0 and visit[nx][ny] <= visit2[x][y] + 1:
                continue
            visit2[nx][ny] = visit2[x][y] + 1
            ji.append((nx,ny))

    return "IMPOSSIBLE"

print(bfs())