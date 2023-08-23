from sys import stdin
import heapq
n = int(input())
heap = []
flag = 0
for _ in range(n):
    a = list(map(int,(stdin.readline().rstrip().split())))

    for i in a:
        if len(heap) < n:
            heapq.heappush(heap,i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
    print(heap)
print(heap[0])