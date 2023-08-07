#틀린문제
n = int(input())
plans = input().split()

x,y =1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

map_types = ['L','R','U','D']
nx = 0
ny = 0
for plan in plans:
    for i in range(len(map_types)):
        if plan == map_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx > n or ny > n:
        continue
    x,y = nx,ny
    print(x,y)
print(x,y)