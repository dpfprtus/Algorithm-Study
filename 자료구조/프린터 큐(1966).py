from collections import deque
num = int(input())

for _ in range(num):
    a,b = map(int,input().split())
    prior = deque(map(int,input().split()))    
    cnt = 0
    while(prior):
        
        prior_max = max(prior)
        first = prior.popleft()
        b -= 1 #찾고자 하는 요소 위치
        if first == prior_max:
            cnt += 1
            if b < 0:
                print(cnt)
                break
        else:
            prior.append(first)
            if b < 0:
                b = len(prior) - 1
        
        
    
    


