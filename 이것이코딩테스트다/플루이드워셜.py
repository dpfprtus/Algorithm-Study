INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for i in range(n+1)]

#대각선 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

#간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

#플루이드 워셜
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()