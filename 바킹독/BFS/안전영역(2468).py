from collections import deque

def bfs(x,y,rain):

    q = deque([(x,y)])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and maps[nx][ny] > rain:
                visit[nx][ny] = 1
                q.append((nx,ny))


n = int(input())


maps = [list(map(int,input().split())) for _ in range(n)]


max_num = 0
dx = [0,1,-1,0]
dy = [1,0,0,-1]


for i in range(n):
    for j in range(n):
        max_num = max(max_num,maps[i][j])

count = 0

for i in range(max_num):
    visit = [[0]*101 for _ in range(101)]
    tmp = 0
    for j in range(n):
        for k in range(n):
            if visit[j][k] == 0 and maps[j][k] > i:
                bfs(j,k,i)
                tmp += 1
    count = max(count,tmp)

print(count)