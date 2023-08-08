from collections import deque
from sys import stdin

num = int(input())
result = deque()
for i in range(0,num):
    a = stdin.readline().split()
    if a[0] == 'push':
        result.append(int(a[1]))
   
    elif a[0] == 'pop':
        if result:
            print(result.pop())
        else: 
            print(-1)
        
    elif a[0] == 'size':
        print(len(result))
       
    elif a[0] == 'empty':
        if result:
            print(0)
        else:
            print(1)

    elif a[0] == 'top':
        if result:
            print(result[-1])
    
        else:
            print(-1)
   
