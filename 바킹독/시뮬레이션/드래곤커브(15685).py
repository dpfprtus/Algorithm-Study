import sys
input = sys.stdin.readline
n = int(input())

maps = [[0]*101 for _ in range(101)]


dx = [0,-1,0,1]
dy = [1,0,-1,0]

def check():
    global result
    for i in range(100):
        for j in range(100):
            if maps[i][j] == 1 and maps[i][j+1] == 1 and maps[i+1][j+1] and maps[i+1][j] == 1:
                result += 1
                
for _ in range(n):
    y,x,d,g = map(int,input().split())
    maps[y][x] = 1
    curve = [d]
    
    for _ in range(g):
        for i in range(len(curve)-1,-1,-1):
            curve.append((curve[i]+1) % 4)

    for i in range(len(curve)):
        y,x = y+dy[curve[i]],x+dx[curve[i]]
        maps[y][x] = 1
    
result = 0
check()
print(result)