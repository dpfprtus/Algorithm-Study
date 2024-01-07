import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    size = list(map(int,input().split()))
    heapq.heapify(size)
    result = 0
    while len(size)>1:
        a = heapq.heappop(size)
        b =  heapq.heappop(size)
        result += a+b
        heapq.heappush(size,a+b)
    print(result)
        
 
        