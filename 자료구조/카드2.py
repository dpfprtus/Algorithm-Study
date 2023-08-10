from collections import deque

num = int(input())
result = deque(range(1,num+1))

while(len(result) > 1):
    
    result.popleft()
    a = result.popleft()
    result.append(a)


print(result[0])
