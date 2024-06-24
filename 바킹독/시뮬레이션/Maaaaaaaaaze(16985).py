import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

#대각선에서 한 대각선까지 가는 최소거리가 12이기 때문에 12가 나오면 탐색 종료

maps = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]

#회전
def maps_rotate(tmp):
    tmp = zip(*tmp[::-1])
    return [list(e) for e in tmp]

def start_rotate(a,i):
    if i == 1:
        return a
    elif i == 2:
        a = maps_rotate(a)
        
    elif i == 3:
        a = maps_rotate(a)
        a = maps_rotate(a)
    else:
        a = maps_rotate(a)
        a = maps_rotate(a)
        a = maps_rotate(a)
    return a
#bfs

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(x,y,z,tmp):
    q = deque([(x,y,z)])
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
  
    while q:
        x,y,z = q.popleft()
    
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            
            if nx < 0 or ny < 0 or nz < 0 or nx >= 5 or ny >= 5 or nz >= 5:
                continue
            if nx == 4 and ny == 4 and nz == 4:
                return visited[z][x][y]+1
            if tmp[nz][nx][ny] == 0 or visited[nz][nx][ny] > 0:
                continue
                
            q.append([nx,ny,nz])
            visited[nz][nx][ny] = visited[z][x][y] + 1       
    return 0
#탐색
ans = [0]*5
result = float("inf")
ans2 = [0]*5
visited = [0]*5

def func2(k,tmp):
    global result
    if k == 5:
        tmp2 = deepcopy(tmp)
        answer = 0
        for idx,value in enumerate(ans2):
            tmp2[idx] = tmp[value]
        if tmp2[0][0][0] == 1 and tmp2[4][4][4] == 1:
            answer = bfs(0,0,0,tmp2)

        if answer != 0:
            result = min(result,answer)
        return 
    
    for i in range(5):
        if visited[i] == 0:
            ans2[k] = i
            visited[i] = 1
            func2(k+1,tmp)
            visited[i] = 0

def func(k):

    if k == 5:
        tmp = deepcopy(maps)
        for idx,j in enumerate(ans):
            tmp[idx] = start_rotate(tmp[idx],j)
        func2(0,tmp)
        return
    
    for i in range(1,5):
        ans[k] = i
        func(k+1)
        
func(0)
if result == float("inf"):
    print(-1)
else:
    print(result)