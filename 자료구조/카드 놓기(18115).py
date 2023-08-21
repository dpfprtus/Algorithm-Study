from collections import deque

n = int(input())
order = list(map(int,input().split()))
dq = deque()
order.reverse()
for i in range(n):
    if order[i] == 1:
        dq.appendleft(i+1)
    elif order[i] == 2:
        a = dq.popleft()
        dq.appendleft(i+1)
        dq.appendleft(a)
    elif order[i] == 3:
        dq.append(i+1)


            
print(' '.join(map(str,dq)))