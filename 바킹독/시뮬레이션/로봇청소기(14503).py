import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
 
result = 1
direction = d
visited = [[0]*m for _ in range(n)]
visited[r][c] = 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]
#빈칸 확인
def find(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 0:
            return True
    return False

def bfs():
    global direction,result
    x,y = r,c
    while True:
        if find(x,y):
            a,b = x,y
            if direction == 0:
                y-=1
                direction = 3
            elif direction == 1:
                x -=1
                direction = 0
            elif direction == 2:
                y +=1
                direction = 1
            elif direction == 3:
                x += 1
                direction = 2

            if visited[x][y] == 0 and maps[x][y] == 0 and 0<=x < n and 0<=y <m:
                visited[x][y] = 1
                result += 1
            else:
                x,y = a,b

        else:
            a,b = x,y
            if direction == 0:
                x+=1
  
            elif direction == 1:
                y-=1
            
            elif direction == 2:
                x-=1
             
            elif direction == 3:
                y+=1
        
            if maps[x][y] == 1 or x < 0 or y<0 or x >=n or y >=m:
                return
            if visited[x][y] == 0:
                visited[x][y] = 1
                result += 1

bfs()
print(result)
