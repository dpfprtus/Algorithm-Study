import heapq
import sys,heapq
input = sys.stdin.readline
for _ in range(int(input())):
    min_heap = []
    max_heap = []
    visited = [0]*(1000001)
    for i in range(int(input())):
        a,b = input().split()
        b = int(b)
        
        if a == "I":
            heapq.heappush(min_heap,(b,i))
            heapq.heappush(max_heap,(-b,i))
            visited[i] = 1
        elif a == "D":
            if b == 1:
                while max_heap and visited[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    value,idx = heapq.heappop(max_heap)
                    visited[idx] = 0
            else:
                while min_heap and visited[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    value,idx = heapq.heappop(min_heap)
                    visited[idx] = 0
        while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
        while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
            
                

    