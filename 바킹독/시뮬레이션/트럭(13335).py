import sys

input= sys.stdin.readline

#n은 트럭의수, w는 다리의 길이, l은 최대 하중
n,w,l = map(int,input().split())
weight = list(map(int,input().split()))

bridge = [0]*w
time = 0
while bridge:
    bridge.pop(0)
    time += 1
    
    if weight:
        if sum(bridge) + weight[0] <= l:
            bridge.append(weight.pop(0))
        else:
            bridge.append(0)
print(time)

                
                
    
    

        
    
