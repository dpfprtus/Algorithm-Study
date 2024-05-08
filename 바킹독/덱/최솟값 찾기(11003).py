import heapq
from collections import deque

N,L = map(int,input().split())

nums = list(map(int,input().split()))
result = deque([])

for i in range(N):
    if result and result[0][0] <= i-L:
        result.popleft()
    
    while len(result) >= 1 and nums[i] < result[-1][1]:
        result.pop() 
    
    result.append((i,nums[i]))

    print(result[0][1],end =" ")