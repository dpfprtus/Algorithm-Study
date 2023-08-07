import heapq
import sys
#시간초과가 발생하여 min,max heap을 따로 구현하여 동기화시켜줘야한다.

for _ in range(int(input())):

    min_heap,max_heap = [],[]
    value = [False] * 1000001
    key = int(input())
    for i in range(key):
        a,b = sys.stdin.readline().split()
        if a == "I":
            heapq.heappush(min_heap,(int(b),i))
            heapq.heappush(max_heap,(-int(b),i))
            value[i] = True
        elif int(b) == 1:
            while max_heap and not value[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                value[max_heap[0][1]] = False
                heapq.heappop(max_heap)
            
        else:
            while min_heap and not value[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                value[min_heap[0][1]] = False
                heapq.heappop(min_heap)
           
    while max_heap and not value[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not value[min_heap[0][1]]:
        heapq.heappop(min_heap)        
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')