from sys import stdin

top = int(input())
razer = list(map(int,stdin.readline().rstrip().split()))
result = []
answer = []

#완전 탐색으로 하니까 시간초과뜸.
for i in range(top):
    while(result):
        if result[-1][1] > razer[i]:
            answer.append(result[-1][0] + 1)
            break
        else:
            result.pop()
    if not result:
        answer.append(0)
    result.append([i,razer[i]])
    
print(' '.join(map(str,answer)))
