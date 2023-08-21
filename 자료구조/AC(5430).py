from collections import deque
from sys import stdin
test = int(input())

for _ in range(test):
    p = input().rstrip()
    n = int(input())
    first = stdin.readline().rstrip()
    first = first[1:-1]
    result = ""
    cnt = 0
    if first == "":
        result = "error" 
        continue
    else:
        integer = deque(map(int,(first.split(","))))
    
    if n == 0:
        integer = []
    
    for i in p:
        if i == "R":
            cnt += 1
    
        elif i == "D":
            if integer:
                if cnt % 2 == 0:
                    integer.popleft()
                else:
                    integer.pop()
            else:
                result = "error"
                break
    
    if result == "error":
        print(result)
    else:
        if cnt % 2 != 0:
            integer.reverse()
            integer = ','.join(map(str,integer))
        else:
            integer = ','.join(map(str,integer))
   
        print("["+integer+"]")

        