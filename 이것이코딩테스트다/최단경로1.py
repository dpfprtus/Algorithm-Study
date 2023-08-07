INF = int(1e9)

n,m = map(int,input().split())

road = [[INF] * (n+1) for i in range(n+1)]
#자기자신에서 자기자신으로 가는건 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            road[a][b] =0
            
for i in range(m):
    a,b = map(int,input().split())
    road[a][b] = 1
    road[b][a] = 1


x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            road[a][b] = min(road[a][b],road[a][k]+road[k][b])

if road[1][k]+road[k][x] >= INF:
    print(-1)
else:
    print(road[1][k]+road[k][x])