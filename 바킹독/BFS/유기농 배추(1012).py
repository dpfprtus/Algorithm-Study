from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()   
        maps[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= 50 and 0 <= ny <= 50 and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = 0


for _ in range(int(input())):
    m,n,k = map(int,input().split())
    maps = [[0]*51 for _ in range(51)]
    visit = maps
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque([])
    count = 0


    for _ in range(k):
        x,y = map(int,input().split())
        maps[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if maps[j][i] == 1:
                bfs(j,i)
                count += 1

    print(count)
   


