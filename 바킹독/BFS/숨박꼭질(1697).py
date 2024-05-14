from collections import deque

n,k = map(int,input().split())
visit = [0] * 200001
q = deque([n])

dx = [-1,1,2]

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            return visit[x]
    
        for i in range(3):
            if dx[i] == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]

            if 0 <= nx <= 200000 and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                q.append(nx)          
        
print(bfs())