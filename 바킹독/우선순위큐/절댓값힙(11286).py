import heapq,sys
input = sys.stdin.readline
n = int(input())
q = []
q2 = []
for _ in range(n):
    a = int(input())
    if a > 0:
        heapq.heappush(q,a)
    elif a < 0:
        heapq.heappush(q2,-a)
    else:
        if q and not q2:
            print(heapq.heappop(q))
        elif q2 and not q:
            print(-heapq.heappop(q2))
        elif not q2 and not q:
            print(0)
        else:
            if q[0] >= q2[0]:
                print(-heapq.heappop(q2))
            elif q[0] < q2[0]:
                print(heapq.heappop(q))
 

            