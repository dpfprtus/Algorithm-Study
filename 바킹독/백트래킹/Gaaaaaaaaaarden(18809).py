import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M,G,R = map(int,input().split())


garden = []
stack = []
INF = 9876543210
answer = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]


for x in range(N):
    garden.append(list(map(int, input().split())))
    for y in range(M):
        if garden[x][y] == 2:
            stack.append((x,y))
            
def solv():
    select = [0]*(G+R)
    for pos in combinations(stack,G+R):
        func(pos,[G,R],0,select)
        
    print(answer)
    
def point_validator(x,y,visited):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    elif visited[x][y] == INF:
        return False
    elif garden[x][y] == 0:
        return False
    return True
   
def bfs(pos,order):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    
    flower_cnt = 0
    for i in range(R+G):
        x,y = pos[i]
        color = order[i]
        visited[x][y] = color
        q.appendleft((x,y,color))
        
    while q:
        x,y,t = q.pop()
        
        if visited[x][y] == INF:
            continue
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if point_validator(nx,ny,visited):
                if visited[nx][ny] == 0:
                    if t > 0:
                        visited[nx][ny] = t+1
                        q.appendleft((nx,ny,t+1))
                    else:
                        visited[nx][ny] = t-1
                        q.appendleft((nx,ny,t-1))
                elif abs(visited[nx][ny]) == abs(t)+1 and ((t < 0 and visited[nx][ny] > 0) or (t > 0 and visited[nx][ny] < 0)):
                    flower_cnt += 1
                    visited[nx][ny] = INF
    return flower_cnt

def func(pos,cnt,now,selected):
    global answer;
    if now == R+G:
        answer = max(bfs(pos,selected),answer)
        return
    
    if cnt[0] > 0:
        cnt[0] -= 1
        selected[now] = 1
        func(pos,cnt,now+1,selected)
        cnt[0] += 1
    
    if cnt[1] > 0:
        cnt[1] -= 1
        selected[now] = -1
        func(pos,cnt,now+1,selected)
        cnt[1] += 1
        
selected = [0]*(G+R)

solv()