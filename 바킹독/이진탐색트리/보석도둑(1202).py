import heapq

n,k = map(int,input().split())
jew = []
for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(jew,(a,b))

weights = [int(input()) for _ in range(k)]
weights.sort()
result = 0

tmp = []
for weigth in weights:
    
    while jew and weigth >= jew[0][0]:
        heapq.heappush(tmp,-heapq.heappop(jew)[1])
    if tmp:
        result -= heapq.heappop(tmp)
    elif not jew:
        break
print(result)

