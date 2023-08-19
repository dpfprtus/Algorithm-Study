from collections import deque


a,b = map(int,input().split())
q = deque(range(1,a+1))
num = list(map(int,input().split()))
result = 0
for i in range(len(num)):
    while True:
        if num[i] == q[0]:
            q.popleft()
            break
        if q.index(num[i]) > len(q) // 2:
            result += len(q)-q.index(num[i])
            q.rotate(len(q)-q.index(num[i]))
        else:
            result += q.index(num[i])
            q.rotate(-q.index(num[i]))
            
print(result)