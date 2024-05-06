from collections import deque

n,m = map(int,input().split())
nums = list(map(int,input().split()))
dq = deque([i for i in range(1,n+1)])
result = 0

for i in nums:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq) / 2:
                while dq[0] != i:
                    a = dq.popleft()
                    dq.append(a)
                    result += 1
            else:
                while dq[0] != i:
                    a = dq.pop()
                    dq.appendleft(a)
                    result += 1
            

print(result) 


