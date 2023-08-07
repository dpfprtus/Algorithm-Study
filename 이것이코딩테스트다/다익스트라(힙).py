import heapq
import sys
intput = sys.stdin.readline
INF = int(1e9)
#노드, 간선
n,m = map(int,input().split())

start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#heapq를 이용했기에 get_smallest_node() 함수는 필요없다.

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
