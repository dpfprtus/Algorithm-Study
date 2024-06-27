import sys
input = sys.stdin.readline
n,m = map(int,input().split())

nums = [list(map(int,input().split())) for _ in range(n)]
result = 0

visited = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
#최댓값 구하기
def dfs(x,y,tmp,count):
    global result

    if count == 4:
        result = max(result,tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny,tmp + nums[nx][ny],count + 1)
            visited[nx][ny] = 0

def exec(x,y):
    global result
    for i in range(4):
        tmp = nums[x][y]

        for j in range(3):
            k = (i+j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if not( 0<= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += nums[nx][ny]
        result = max(result,tmp)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,nums[i][j],1)
        visited[i][j] = 0
        exec(i,j)

print(result)