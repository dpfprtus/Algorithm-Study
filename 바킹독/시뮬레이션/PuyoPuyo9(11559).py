import sys
from collections import deque

input = sys.stdin.readline

maps = []
dx = [0,0,1,-1]
dy = [-1,1,0,0]

#R,G,B,P,Y
#뿌요 지우기
def bfs(color_x,color_y):
    q = deque([(color_x,color_y)])
    visited = [[0]*6 for _ in range(12)]
    cnt = 0

    while q:
        x,y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6 or visited[nx][ny] == 1 or maps[nx][ny] != maps[color_x][color_y]:
                continue
            
            visited[nx][ny] = 1
            cnt += 1
            q.append((nx,ny))
    
    if cnt >= 3:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    maps[i][j] = '.'
        return 1
    return 0


#뿌요 맨 밑으로 내리기
def down():
    
    tmp = [["."]*6 for _ in range(12)]
    for j in range(6):
        idx = 11
        for i in range(11,-1,-1):
            if maps[i][j] != '.':
                tmp[idx][j] = maps[i][j]
                idx-=1

    return tmp

for i in range(12):
    maps.append(list(input().rstrip()))

result = 0

while True:

    tmp = 0
    flag = 0

    for i in range(12):
        for j in range(6):
            if maps[i][j] != '.':
                tmp = bfs(i,j)
                if tmp == 1:
                    flag = 1
    if flag == 1:
        result += 1
    else:
        break
    maps = down()

print(result)