import sys,heapq
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    visited = [False] * 1000001
    for i in range(k):
        a,b = input().rstrip().split()
        if a == "I":
            heapq.heappush(max_heap,(-int(b),i))
            heapq.heappush(min_heap,(int(b),i))
            visited[i] = True
        elif a == "D":
            if int(b) == 1: #최댓값 삭제
               
                while min_heap and visited[min_heap[0][1]] != True:
                    heapq.heappop(min_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                     
              
            else: #최솟값 삭제
                
                while max_heap and visited[max_heap[0][1]] != True:
                    heapq.heappop(max_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
           
    while max_heap and visited[max_heap[0][1]] != True:
        heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] != True:
        heapq.heappop(min_heap)
    if min_heap and max_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
    
