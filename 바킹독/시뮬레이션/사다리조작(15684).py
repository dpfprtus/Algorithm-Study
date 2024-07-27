import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())
sadari = [[0]*n for _ in range(h)]
for i in range(m):
    a,b = map(int,input().split())
    sadari[a-1][b-1] = 1

def check():
    for i in range(n):
        start = i
        for j in range(h):
            if sadari[j][start] == 1:
                start += 1
            elif start > 0 and sadari[j][start-1] == 1:
                start -= 1
        if i != start:
            return False
    return True

def dfs(cnt,x):
    global result
    if result <= cnt:
        return
    
    if check():
        result = min(cnt,result)
        return
    
    if cnt == 3:
        return
    
    for i in range(x,h):
        for j in range(0,n-1):
            if sadari[i][j] == 0:
                sadari[i][j] = 1
                dfs(cnt+1,i)
                sadari[i][j] = 0
                
result = 4
dfs(0,0)
if result > 3:
    print(-1)
else:
    print(result)