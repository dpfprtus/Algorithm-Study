import heapq
from sys import stdin
n = int(input())
heap = []
heap2 = [] #음수
for _ in range(n):
    a = int(stdin.readline().rstrip())
    b = 0
    c = 0
    if a != 0:
        if a > 0:
            heapq.heappush(heap,a)
        else:
            heapq.heappush(heap2,-a)
    else:
        if heap:
            b =heapq.heappop(heap)
        if heap2:
            c = heapq.heappop(heap2)
        
        if b ==0 and c == 0:
            print(0)
            continue
        if b == 0 and c != 0:
            print(-c)
            continue
        elif b != 0 and c == 0:
            print(b)
            continue
        elif abs(b)>=abs(c):
            print(-c)
            heapq.heappush(heap,b)
        elif abs(b) < abs(c):
            print(b)
            heapq.heappush(heap2,c)
        