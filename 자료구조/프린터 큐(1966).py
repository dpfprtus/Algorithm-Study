from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    prior = deque((enumerate(map(int,input().split()))))
    cnt = 0
    a = 101

    while a != m:
        max_prior = max(prior,key = lambda x:x[1])
        if prior[0][1] == max_prior[1]:
            a = prior.popleft()[0]
            cnt += 1
        else:
            tmp = prior.popleft()
            prior.append(tmp)            
    print(cnt)
    
        
