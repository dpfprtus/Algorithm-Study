#틀린문제

n,m = map(int,input().split())

a,b,dir = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

bangmun = [[0] * m for _ in range(n)]
bangmun[a][b] = 1
count = 1
def turn_left():
    global dir
    dir -= 1
    if dir < 0:
        dir = 3
turn_count = 0

while True:
    turn_left()
    nx = a + dx[dir]
    ny = b + dy[dir]
    if maps[nx][ny] == 0 and bangmun[nx][ny] == 0:
        a = nx
        b = ny
        bangmun[a][b] = 1
        turn_count = 0
        count+=1
        continue
        
    else:
        turn_count += 1
    
    if turn_count == 4:
        nx = a - dx[dir]
        ny = b - dy[dir]
        if bangmun[nx][ny] == 0:
            a = nx
            b = ny
        else:
            break
        turn_count = 0

print(count)

    
    