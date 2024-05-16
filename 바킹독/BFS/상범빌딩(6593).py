from collections import deque

def bfs():
    
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and visit[nz][nx][ny] == 0 and maps_result[nz][nx][ny] != "#" and maps_result[nz][nx][ny] != "S":
                if maps_result[nz][nx][ny] == "E":
                    return "Escaped in " +str(visit[z][x][y] + 1) + " minute(s)."
                visit[nz][nx][ny] = visit[z][x][y] + 1
                q.append((nx,ny,nz))

    return "Trapped!"

while True:
    L,R,C = map(int,input().split())
    if L == R == C == 0:
        break
    
    maps = [[]]
    visit = [[[0]*31 for _ in range(R+1)] for _ in range(L+1)]

    dx = [-1,0,1,0,0,0]
    dy = [0,1,0,-1,0,0]
    dz = [0,0,0,0,1,-1]

    q = deque([])

    maps_result = []
    
    for i in range(L):
        maps = [list(input()) for _ in range(R)]
        maps_result.append(maps)
        for k in range(R):
            for j in range(C):
                if maps_result[i][k][j] == "S":
                    q.append((k,j,i))
        input()

    print(bfs())
    
    
    
    