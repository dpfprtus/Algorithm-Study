import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
time = []

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    

def dikstra(start):
    q = []
    heapq.heappush(q,(0,start))
    global count
    count = 0
    while q:
        dist, now = heapq.heappop(q)
        distance[start] = 0
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                time.append(cost)
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
            count += 1
dikstra(c)

print(count,max(time))