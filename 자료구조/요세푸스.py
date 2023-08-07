from collections import deque

a,b = map(int,input().split())
c = deque(range(1, a + 1))

cnt = 0
result = []

while(c):
    
    num = c.popleft()
    cnt += 1
    if(cnt == b):
        result.append(num)
        cnt = 0
    else:
        c.append(num)  

output = "<" + ", ".join(map(str, result)) + ">"
print(output)   

