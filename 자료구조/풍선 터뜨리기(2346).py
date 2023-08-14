from collections import deque

num = int(input())
bollon = deque(enumerate(map(int,input().split()))) #인덱스를 저장하기 위해 enumerate사용 (0,1),(1,2)...
cnt = 0
idx = 0
result = []
while(bollon):
    index,cnt = bollon.popleft()
    result.append(index+1)
    if cnt > 0:
        bollon.rotate(-(cnt-1))
    else:
        bollon.rotate(-cnt)
print(' '.join(map(str,result)))

    
            
        
        