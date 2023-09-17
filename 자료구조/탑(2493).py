import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
result = []
answer = []
for i in range(n):
    while result:
        if result[-1][1] > top[i]:
            answer.append(result[-1][0]+1)
            break
        else:
            result.pop()
    if not result:
        answer.append(0)
    result.append([i,top[i]])
print(' '.join(map(str,answer)))

            
        
