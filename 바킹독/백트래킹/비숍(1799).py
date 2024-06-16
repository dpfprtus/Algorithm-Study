import sys
input = sys.stdin.readline

n = int(input())
maps = []
can = [[] for i in range(2*n)]


for i in range(n):
    maps.append(list(map(int,input().split())))
    for j in range(n):
        if maps[i][j] == 1:
            can[i+j].append((i,j))
            
L = 2*n-1

visited = [0]*(L+1)

def func(now,cnt):
    global ans
    if now >= L:
        ans = max(ans,cnt)
        return
    
    if ans >= (cnt + (L-now+1)//2):
        return
    
    for i,j in can[now]:
        if visited[i-j] == 0:
            visited[i-j] = 1
            func(now+2,cnt+1)
            visited[i-j] = 0
    func(now+2,cnt)
    
ans = 0
func(0,0)
tmp = ans
ans = 0
func(1,0)
print(ans+tmp)
            
    
            
    
