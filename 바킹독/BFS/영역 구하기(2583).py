from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    count = 1
    visit[x][y] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0 and maps[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                maps[nx][ny] = 1
                count += 1
                q.append((nx,ny))
    return count

m,n,k = map(int,input().split())
maps = [[0] * (n) for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int,input().split(" "))

    for i in range(m-d,m-b):
        for j in range(a,c):
            maps[i][j] = 1

visit = [[0]*101 for _ in range(101)]
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]
count = 0
result = []

for i in range(m):
    for j in range(n):
        if maps[i][j] == 0:
            result.append(bfs(i,j))
            count += 1

print(count)
print(*sorted((result)))


