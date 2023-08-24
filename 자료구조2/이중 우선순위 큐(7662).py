import heapq
from sys import stdin

t = int(input())

for _ in range(t):
    k = int(input())
    visited = [False]*1_000_001
    heap = []
    heap2 = []
    for i in range(k):
        a,b = stdin.readline().rstrip().split()
        if a == "I":
            heapq.heappush(heap2,(-int(b),i)) #최댓값
            heapq.heappush(heap,(int(b),i)) #최솟값
            visited[i] = True
        elif a == "D":
            if int(b) == -1:
                while heap and not visited[heap[0][1]]:
                    heapq.heappop(heap)
                if heap:
                    visited[heap[0][1]] = False
                    heapq.heappop(heap)
                  
            elif int(b) == 1:
                while heap2 and not visited[heap2[0][1]]:
                    heapq.heappop(heap2)
                if heap2:
                    visited[heap2[0][1]] = False
                    heapq.heappop(heap2)
    while heap and not visited[heap[0][1]]:heapq.heappop(heap)
    while heap2 and not visited[heap2[0][1]]:heapq.heappop(heap2)
    if heap and heap2:
        print(-heap2[0][0],heap[0][0])
        
    else:
        print("EMPTY")
