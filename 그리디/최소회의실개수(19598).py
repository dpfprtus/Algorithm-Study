import sys,heapq
input = sys.stdin.readline
n = int(input())
meet = [list(map(int,input().split())) for _ in range(n)]

meet.sort(key = lambda x:(x[0],x[1]))
cnt = 1
heap = [meet[0][1]]
for i in range(1,len(meet)):
    start,end = meet[i]
    if start < heap[0]:
        heapq.heappush(heap,end)
        cnt += 1
    else:
        heapq.heappop(heap)
        heapq.heappush(heap,end)
print(cnt)