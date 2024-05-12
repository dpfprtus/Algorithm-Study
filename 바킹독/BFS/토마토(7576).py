from collections import deque

import sys
input = sys.stdin.readline

m,n = map(int,input().split())
visit = [[0] *1001 for _ in range(1001)]
box = [list(map(int,input().split())) for _ in range(n)]

tomato = deque([])
dx = [-1,0,1,0]
dy = [0,-1,0,1]
max_num = 0
flag = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((i,j))

while tomato:
    x,y = tomato.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if box[nx][ny] == -1 or visit[nx][ny] >= 1 or box[nx][ny] == 1:
            continue
        box[nx][ny] = 1
        tie = 1
        visit[nx][ny] = visit[x][y] + 1
        max_num = max(max_num, visit[nx][ny])
        tomato.append((nx,ny))


for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            flag = 1
            break
if flag:
    print(-1)
else:   
    print(max_num)