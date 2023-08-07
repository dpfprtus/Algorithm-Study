import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)]

visted = [False] * (n+1)
distance = [INF] * (n+1)

#간선 정보 입력
for _ in range(m):
    a, b, c = map(int,input().split())
    #a노드에서 b노드 까지 가는데 c비용이 듬
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visted[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visted[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1]
    #시작 노드를 제외하고 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visted[now] = True
        #현재 노드와 연결된 다른 노드 체크
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로  l이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)     

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i]) 
