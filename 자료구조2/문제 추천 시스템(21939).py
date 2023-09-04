import heapq
from sys import stdin

n = int(input())
max_heap = []
min_heap = []
visited = [False]*100_001
for _ in range(n):
    a,b = map(int,input().split())
    heapq.heappush(min_heap,(b,a))
    heapq.heappush(max_heap,(-b,-a))
    visited[a] = True

for i in range(int(input())):
    s = stdin.readline().rstrip().split()
    if s[0] == "add":
        a = int(s[1])
        b = int(s[2])
        while not visited[-max_heap[0][1]]:heapq.heappop(max_heap)
        while not visited[min_heap[0][1]]:heapq.heappop(min_heap)
        heapq.heappush(min_heap,(b,a))
        heapq.heappush(max_heap,(-b,-a)) 
        visited[a] = True
    elif s[0] == "recommend":
        if s[1] == "1":
            while not visited[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                print(-max_heap[0][1])
        else:
            while not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                print(min_heap[0][1])
    elif s[0] == "solved":
        visited[int(s[1])] = False
    
    