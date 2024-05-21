from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    count = 0
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and maps[nx][ny] == "1":
                visit[nx][ny] = visit[x][y] + 1
                count += 1
                q.append((nx,ny))
    if count == 0 and maps[x][y] == "1":
        result.append(1)
    else:
        result.append(count)

n = int(input())
maps = [input() for _ in range(n)]
visit = [[0]*26 for _ in range(26)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = []
count = 0

for i in range(n):
    for j in range(n):
        if maps[i][j] == "1" and visit[i][j] == 0:
            bfs(i,j)
            count += 1

print(count)
print(*sorted(result),sep="\n")


