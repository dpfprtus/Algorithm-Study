import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

maps = []
red = [[0,0]]
blue = [[0,0]]
goal = [[0,0]]
for i in range(n):
    maps.append(list(input()))
    for j in range(m):
        if maps[i][j] == "R":
            red[0] = [i,j]
        if maps[i][j] == "B":
            blue[0] = [i,j]
        if maps[i][j] == "O":
            goal[0] = [i,j]

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#기울이기
def push(red_x,red_y,blue_x,blue_y):
    q = deque([red_x,red_y])
    visited = [[0]*m for _ in range(n)]

    while q:
        for i in range(4):
            nred_x = red_x + dx[i]
            nred_y = red_y + dy[i]
            blue_x = blue_x + dx[i]
            blue_y = blue_y + dy[i]
            if maps[nred_x][nred_y] == "#":
                continue
            if (blue_x == nred_x and blue_y == nred_y) or visited[nred_x][nred_y] == 1:
                if nred_x == goal[0][0] and nred_y == goal[0][1]:
                    return -1
                continue
            if maps[blue_x][blue_y] == "#":
                blue_x -= dx[i]
                blue_y -= dy[i]
            
            visited[nred_x][nred_y] = visited[red_x][red_y] + 1
            if nred_x == goal[0][0] and nred_y == goal[0][1]:
                return visited[nred_x][nred_y]
            
            if visited[nred_x][nred_y] > 10:
                return -1
            q.append([nred_x,nred_y])
    return -1

print(push(red[0][0],red[0][1],blue[0][0],blue[0][1]))
#경우의 수