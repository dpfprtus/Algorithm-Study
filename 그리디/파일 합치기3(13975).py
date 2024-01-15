import sys, heapq
input = sys.stdin.readline

for _  in range(int(input())):
    k = int(input())
    file = list(map(int,input().split()))
    heapq.heapify(file)
    result = 0
    while len(file)>1:
        a = heapq.heappop(file)
        b = heapq.heappop(file)
        result += a+b
     
        heapq.heappush(file,a+b)
   
    print(result)
