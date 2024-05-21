from collections import deque

def bfs():

    while fire:
        x,y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and visit_fire[nx][ny] == 0 and maps[nx][ny] != "#" and maps[nx][ny] != "*":
                visit_fire[nx][ny] = visit_fire[x][y] + 1
                fire.append((nx,ny))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                return visit[x][y] + 1

            if visit[nx][ny] == 0 and (visit_fire[nx][ny] == 0  or visit_fire[nx][ny] > visit[x][y] + 1) and maps[nx][ny] == ".":
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))

    return "IMPOSSIBLE"

for _ in range(int(input())):
    w,h = map(int,input().split())
    maps = [input() for _ in range(h)]

    q = deque([])
    fire = deque([])
    visit = [[0]*1001 for _ in range(1001)]
    visit_fire = [[0]*1001 for _ in range(1001)]
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == "@":
                q.append((i,j))
            elif maps[i][j] == "*":
                fire.append((i,j))
    print(bfs())

