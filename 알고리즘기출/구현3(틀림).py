n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn_direction(direction,a):
    if a == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction
def simulate():
    x,y = 1,1
    time = 0
    index = 0
    direction = 0
    data[x][y] = 2
    g = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y+ dy[direction]
        if nx <= n and nx >= 1 and ny<=n and ny >= 1 and data[nx][ny] != 2:
            if data[nx][ny] == 1:
                g.append((nx,ny))
                data[nx][ny] = 2
            if data[nx][ny] == 0:
                g.append((nx,ny))
                px,py = g.pop(0)
                data[px][py] = 0
        else:
            time+=1
            break
        x = nx
        y= ny
        time += 1
        if index<l and info[index][0] == time:
            direction = turn_direction(direction,info[index][1])
            index+=1 
    return time
print(simulate())
            