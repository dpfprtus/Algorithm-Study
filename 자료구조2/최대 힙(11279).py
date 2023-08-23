import heapq
from sys import stdin

n = int(input())
heap = []
for _ in range(n):
    a = int(stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(heap,(-a,a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)