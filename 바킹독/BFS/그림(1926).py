from collections import deque
import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n,m = map(int,input().split())
pics = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*502 for _ in range(502)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]
count = []

def bfs(x,y):
    count = 1
    visit[x][y] = 1
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if visit[nx][ny] == 1 or pics[nx][ny] == 0:
                continue
            visit[nx][ny] = 1
            q.append((nx,ny))
            count += 1
    return count

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and pics[i][j] == 1:
            count.append(bfs(i,j))

print(len(count))
if len(count) > 0:
    print(max(count))
else:
    print(0)

