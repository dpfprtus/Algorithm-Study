from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    flag = 0
    isReversed = 0
    
    if n == 0:
        arr = input()
        arr = [] 
    else:
        arr = deque(map(int,input().rstrip()[1:-1].split(',')))
    
    for i in p:
        if i == "R":
            isReversed = not isReversed
        else:
            if arr:
                if isReversed == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                flag = 1
                break
    if flag == 1:
        print("error")
    else:
        if isReversed == 1:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("[" + ",".join(arr) + "]")

    

