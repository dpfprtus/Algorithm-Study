from collections import deque

v,e = map(int,input().split())

#모든 노드에 대한 진입 차수를 0으로 설정
indegree = [0] * (v+1)

#각 노드에 연결된 간선 정보가 들어간 연결리스트 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    #처음 시작할 떄는 진입차수가 0인 노드를 큐에 삽입
    
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
            
        for i in graph[now]:
                
            indegree[i] -= 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                    
    for i in result:
        print(i,end=' ')

topology_sort()