from collections import deque

n = int(input())
a = list(map(int,input().split()))
a.reverse()
result = deque()

for i in range(n):
    if a[i] == 1:
        result.appendleft(i+1)
    elif a[i] == 2:
        b = result.popleft()
        result.appendleft(i+1)
        result.appendleft(b)
    else:
        result.append(i+1)
print(' '.join(map(str,result)))