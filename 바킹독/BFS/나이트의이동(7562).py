from collections import deque

def bfs():
    
    while q:
        x,y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<length and 0 <= ny < length and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
                if nx == x_result and ny == y_result:
                    return visit[nx][ny]


for _ in range(int(input())):
    length = int(input())
    x,y = map(int,input().split())
    x_result, y_result = map(int,input().split())

    if x == x_result and y == y_result:
        print(0)
        continue

    visit = [[0]*length for _ in range(length)]
    q = deque([(x,y)])

    dx = [-2,-1,-2,-1,2,1,2,1]
    dy = [-1,-2,1,2,-1,-2,1,2]

    print(bfs())





