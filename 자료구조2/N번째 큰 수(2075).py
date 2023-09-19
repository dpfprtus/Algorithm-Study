import sys,heapq
input = sys.stdin.readline

n = int(input())
a = []
heap = []

for i in range(n):
    a = map(int,input().split())
    for j in a:
        if len(heap) < n:
            heapq.heappush(heap,j)
        else:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap,j)

print(heap[0])