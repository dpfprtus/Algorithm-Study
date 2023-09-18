from collections import deque

n = int(input())
ballon = deque(enumerate(map(int,input().split())))
result = []
for i in range(n):
    first = ballon.popleft()
    result.append(first[0]+1)
    if first[1] > 0:
        ballon.rotate(-first[1]+1)
    else:
        ballon.rotate(-first[1])
    print(ballon)
        
print(' '.join(map(str,result)))