import sys
import copy
input = sys.stdin.readline

n,m = map(int,input().split())
maps = []
cctv = []

brick = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    maps.append(list(map(int,input().split())))
    for j in range(m):
        if 1<= maps[i][j] <= 5: 
            cctv.append([i,j])
        elif maps[i][j] == 6:
            brick += 1
cctv_length = len(cctv)
ans = [0]*cctv_length

def direction(x,y,dir,space_maps):
    
    dir %= 4
    nx,ny = x, y
    tmp = 0
    
    while True:
        nx += dx[dir]
        ny += dy[dir]
        if nx < 0 or ny < 0 or nx >=n or ny >= m or space_maps[nx][ny] == 6:
            break
        if space_maps[nx][ny] != 0:
            continue
        tmp += 1
        space_maps[nx][ny] = "#"
    return tmp

result_answer = 65

def func(k):
    
    global result_answer
    result = 0
    space_maps = [[j for j in maps[i]] for i in range(n)]
    space_maps = [[j for j in maps[i]] for i in range(n)]
    
    if k == cctv_length:
        
        for idx,i in enumerate(ans):
            x,y = cctv[idx]
            if maps[x][y] == 1:
                result += direction(x,y,i,space_maps)
                    
            elif maps[x][y] == 2:
                result +=direction(x,y,i,space_maps)
                result +=direction(x,y,i+2,space_maps)

            elif maps[x][y] == 3:
                    
                result +=direction(x,y,i,space_maps)
                result +=direction(x,y,i+1,space_maps)
                    
            elif maps[x][y] == 4:
                result +=direction(x,y,i,space_maps)
                result +=direction(x,y,i+1,space_maps)
                result +=direction(x,y,i+2,space_maps)
            elif maps[x][y] == 5:
                result +=direction(x,y,i,space_maps)
                result +=direction(x,y,i+1,space_maps)
                result +=direction(x,y,i+2,space_maps)
                result +=direction(x,y,i+3,space_maps)

        result_tmp = n*m - brick - cctv_length - result
        result_answer = min(result_answer,result_tmp)
        return
    
    for i in range(4):
        ans[k] = i
        func(k+1)
        
func(0)
print(result_answer)


