import heapq
import sys
input = sys.stdin.readline
n = int(input())
room = [list(map(int,input().split(' '))) for _ in range(n)]
room.sort(key = lambda x:x[0])
heap = [room[0][1]]
cnt = 1

for i in range(1,len(room)):
    start,end = room[i]
    if start >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,end)
    else:
        heapq.heappush(heap,end)
        cnt += 1


print(cnt)
